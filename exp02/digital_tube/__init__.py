from .draw import *
from .draw_async import *

__doc__ = """
七 (八) 段数码管显示模块

        author: (c) 2024 Vincy SHI | 史云昔
        date: 2024-06-16

    本模块使用 Python 标准库 turtle 实现了七 (八) 段数码管绘制模块，支持任意16进制数字小数点显示，支持异步显示。

    模块对外提供了三个函数: 
        digital_tube: 直接操作默认 turtle 画笔绘制，同时也用于传入非默认 turtle 画笔绘制.
        digital_tube_async: 异步绘制，支持传入非默认 turtle 画笔和直接操作 turtle 画笔. 不会阻塞, 需要 python async 协程事件循环.
        digital_tube_await: 异步绘制的同步阻塞版本，同时也用于传入非默认 turtle 画笔绘制.

    支持的字符集: 
        0-9, A-F, a-f, 空格 (可表示为空格符或下划线), 小数点 (可表示为小数点或字母 p/P), 换行符 (\\n).
    支持的对齐方式: 
        "left", "center", "right".
    支持的字体风格: 
        标准 (normal), 斜体 (italic). 所有的字体风格都是等宽字体, 且高度和宽度比例为 1:0.75
    支持的刷新级别 (仅在已设置 tracer 时有效): 
        全部绘制完成后刷新 (digital), 每行刷新 (line), 每个字符刷新 (char), 字符的每一笔绘制完后刷新 (path), 不自动刷新 (None).

    其余属性 (描边颜色, 填充颜色, 线宽, 起笔位置等) 继承自画笔本身, 请直接操作 turtle 画笔进行设置.
    函数的详细参数和返回值请参考函数文档字符串. 
"""

__all__ = ["digital_tube", "digital_tube_await", "digital_tube_async"]
