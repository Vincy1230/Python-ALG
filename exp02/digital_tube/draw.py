from ._digital_tube import *
import turtle as t

__all__ = [
    "digital_tube",
    "_digital_tube_line",
    "_digital_tube_char",
    "_digital_tube_path",
]


def digital_tube(
    digitals: str,
    move: bool = False,
    align: _Align = "left",
    font: _Font = (72, "normal"),
    frame: bool = False,
    line_height: float = 1.25,
    refresh_level: _RLevel = None,
    pen: t.Turtle = t.getturtle(),
) -> None:
    """
    直接操作默认 turtle 画笔绘制，同时也用于传入非默认 turtle 画笔绘制.
    :param digitals: 要绘制为数码管的数字字符串, 支持大小写16进制数字(0-9/a-f/A-F), 小数点(./p/P), 空格( /_)和换行符(\\n).
    :param move: 绘制完成后画笔(是/否)移动到最后一个字符的位置. 如果 move 为真值, 画笔会移至文本的右下角. 默认情况下 move 为 False.
    :param align: 字符串 "left", "center" 或 "right". 将文本指定对齐并绘制在当前画笔位置.
    :param font: 一个二元组 (font_size, font_style). font_size 支持以整数表示的字高, font_style 支持 "normal" 和 "italic".
    :param frame: (是/否)绘制数码管不亮的部分.
    :param line_height: 存在多行时, 设置行高.
    :param refresh_level: 刷新级别, "path", "char", "line", "digital", None, 仅在已设置 tracer() 时有效.
    :param pen: 传入 turtle.Turtle 对象. 默认采用当前画布默认的 turtle 画笔.
    :return: None
    """
    args_check(digitals, align, font[1], refresh_level)
    _align_dict = {"left": "<", "center": "^", "right": ">"}
    lines = digitals.split("\n")
    max_len = max(len_line(line) for line in lines)
    lines = [
        f"{line:{_align_dict[align]}{len(line)+max_len-len_line(line)}}"
        for line in lines
    ]
    ipen_isdown, ipen_isvisible = pen.isdown(), pen.isvisible()
    pen.penup()
    pen.hideturtle()
    pos_list = [
        pen.pos() + t.Vec2D(0, (len(lines) - i - 1) * line_height * font[0])
        for i in range(len(lines))
    ]
    for pos, line in zip(pos_list[:-1], lines[:-1]):
        pen.goto(pos)
        _digital_tube_line(
            line,
            move=False,
            align=align,
            font=font,
            frame=frame,
            refresh_level=refresh_level,
            pen=pen,
        )
    pen.goto(pos_list[-1])
    if ipen_isdown:
        pen.pendown()
    if ipen_isvisible:
        pen.showturtle()
    _digital_tube_line(
        lines[-1],
        move=move,
        align=align,
        font=font,
        frame=frame,
        refresh_level=refresh_level,
        pen=pen,
    )
    if refresh_level == "digital":
        t.update()


def _digital_tube_line(
    line: str,
    move: bool = False,
    align: _Align = "left",
    font: _Font = (72, "normal"),
    frame: bool = False,
    refresh_level: _RLevel = None,
    pen: t.Turtle = t.getturtle(),
) -> None:
    """绘制一行数码管字符."""
    line = line.lower().replace(" ", "_")
    font_size, _ = font
    ipen_isdown, ipen_pos, ipen_isvisible = pen.isdown(), pen.pos(), pen.isvisible()
    pos_list = words_pos(ipen_pos, line, align, font_size)
    line += "x"
    pen.hideturtle()
    i = 0
    for char in range(1, len(line)):
        if line[char] in CTRL_CH:
            _digital_tube_char(
                line[char - 1],
                font,
                pos_list[i],
                pt=True,
                frame=frame,
                refresh_level=refresh_level,
                pen=pen,
            )
        elif line[char - 1] in CTRL_CH:
            continue
        else:
            _digital_tube_char(
                line[char - 1],
                font,
                pos_list[i],
                pt=False,
                frame=frame,
                refresh_level=refresh_level,
                pen=pen,
            )
        i += 1
    pen.penup()
    pen.goto(ipen_pos)
    if ipen_isdown:
        pen.pendown()
    if ipen_isvisible:
        pen.showturtle()
    if move:
        pen.goto(pos_list[-1])
    if refresh_level == "line":
        t.update()


def _digital_tube_char(
    char: str,
    font: _Font,
    pos: t.Vec2D,
    pt: bool = False,
    frame: bool = False,
    refresh_level: _RLevel = None,
    pen: t.Turtle = t.getturtle(),
) -> None:
    """绘制一个数码管字符."""
    font_size, font_style = font
    mapper = Mapper(pos, font_size)
    paths = CHAR_SET[char] | {"p"} if pt else CHAR_SET[char]
    for path in paths:
        _digital_tube_path(
            mapper,
            NODES_SET[font_style][path],
            fill=True,
            refresh_level=refresh_level,
            pen=pen,
        )
    if frame:
        for path in PATH_NAME_SPACE - paths:
            _digital_tube_path(
                mapper,
                NODES_SET[font_style][path],
                fill=False,
                refresh_level=refresh_level,
                pen=pen,
            )
    if refresh_level == "char":
        t.update()


def _digital_tube_path(
    mapper: Mapper,
    path: _Path,
    fill: bool = True,
    refresh_level: _RLevel = None,
    pen: t.Turtle = t.getturtle(),
) -> None:
    """绘制数码管字符的一条."""
    pen.penup()
    pen.goto(mapper(path[-1]))
    pen.pendown()
    if fill:
        pen.begin_fill()
    for j in path:
        pen.goto(mapper(j))
    if fill:
        pen.end_fill()
    if refresh_level == "path":
        t.update()


if __name__ == "__main__":
    t.fd(-200)
    t.speed(0)
    t.tracer(0)
    digital_tube("114.514\n1919810", move=True, frame=True, pen=t.clone())
    t.update()
    t.done()
