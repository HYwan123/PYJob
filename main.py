import asyncio
import os
from playwright.async_api import async_playwright
from rich.console import Console
from rich.panel import Panel

console = Console()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        try:
            storage_state_path = "auth.json"

            # Check if a storage state file exists.
            if os.path.exists(storage_state_path):
                console.print(Panel(f"✅ 找到状态文件 [bold green]{storage_state_path}[/bold green]，将使用它来恢复登录状态。", title="[bold cyan]登录状态[/bold cyan]", border_style="green"))
                context = await browser.new_context(storage_state=storage_state_path)
            else:
                console.print(Panel(f"⚠️ 未找到状态文件 [bold yellow]{storage_state_path}[/bold yellow]，将进行手动登录。", title="[bold cyan]登录状态[/bold cyan]", border_style="yellow"))
                context = await browser.new_context()

            page = await context.new_page()

            await page.goto("https://www.zhipin.com/web/geek/jobs?city=101020100&jobType=1902&degree=203&query=%E8%BF%90%E7%BB%B4")

            # If the storage state file didn't exist, we need to log in and save the state.
            if True: #not os.path.exists(storage_state_path):
                title = await page.title()
                console.print(f"📄 页面标题: [bold]{title}[/bold]")
                console.print(Panel("[bold yellow]脚本已暂停，请在浏览器中手动登录。完成后，在 Playwright Inspector 窗口中点击 'Resume' (继续)按钮。[/bold yellow]", title="[bold red]需要用户操作[/bold red]", border_style="red"))
                # 这将暂停脚本执行，并打开一个检查器工具，方便您进行操作
                await page.pause()

                await context.storage_state(path=storage_state_path)
                console.print(Panel(f"💾 登录状态已成功保存到 [bold green]{storage_state_path}[/bold green]", title="[bold cyan]保存成功[/bold cyan]", border_style="green"))


            while True:
                console.print("\n[bold cyan]新一轮职位处理开始...[/bold cyan]")
                element = await page.locator(".card-area").all()
                console.print(f"🔍 找到 {len(element)} 个职位。")

                for i, e in enumerate(element):
                    console.print(f"\n[bold]处理第 {i+1}/{len(element)} 个职位...[/bold]")
                    await e.click()
                    await page.wait_for_timeout(1000)
                    
                    result = await page.locator(".op-btn-chat").all()
                    if result:
                        await result[0].click()
                        console.print("✅ 已点击'打招呼'。")
                    else:
                        console.print("❌ 未找到'打招呼'按钮，跳过。")

                    await page.wait_for_timeout(1000)
                    
                    cancel_btn = page.locator(".cancel-btn")
                    if await cancel_btn.is_visible():
                        await cancel_btn.click()
                        console.print("✅ 已关闭弹窗。")
                    else:
                        console.print("ℹ️ 未找到弹窗关闭按钮，可能无需关闭。")

                console.print("[bold green]\n本轮操作完成。等待30秒后开始下一轮...[/bold green]")
                await page.wait_for_timeout(30000) # Wait 30 seconds before next round
        
        finally:
            console.print("\n[bold red]正在关闭浏览器...[/bold red]")
            await page.screenshot(path="final_state.png")
            console.print(f"📷 已截取最终屏幕截图: [bold]final_state.png[/bold]")
            await browser.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[bold yellow]脚本被用户中断。正在清理资源...[/bold yellow]")
    except Exception as e:
        console.print(f"\n[bold red]脚本发生错误: {e}[/bold red]")
