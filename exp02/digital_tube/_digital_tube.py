from typing import TypeAlias, Literal, List, Tuple
import turtle as t
import re

__all__ = [
    "_Align",
    "_Font",
    "_Path",
    "_RLevel",
    "DISPLAY_CH",
    "CTRL_CH",
    "CTRL_CH_RESTR",
    "PATH_NAME_SPACE",
    "CHAR_SET",
    "NODES_SET",
    "Mapper",
    "args_check",
    "len_line",
    "words_pos",
]

_Align: TypeAlias = Literal["left", "center", "right"]
_Font: TypeAlias = Tuple[float, Literal["normal", "italic"]]
_Path: TypeAlias = List[t.Vec2D]
_RLevel: TypeAlias = Literal["digital", "line", "char", "path", None]


DISPLAY_CH = set("0123456789abcdefABCDEF _")
CTRL_CH = set(".pP")
CTRL_CH_RESTR = "[.pP]"  # only for re.compile
PATH_NAME_SPACE = set("abcdefgp")

CHAR_SET = {
    "0": set("abcdef"),
    "1": set("bc"),
    "2": set("abdeg"),
    "3": set("abcdg"),
    "4": set("bcfg"),
    "5": set("acdfg"),
    "6": set("acdefg"),
    "7": set("abc"),
    "8": set("abcdefg"),
    "9": set("abcdfg"),
    "a": set("abcefg"),
    "b": set("cdefg"),
    "c": set("adef"),
    "d": set("bcdeg"),
    "e": set("adefg"),
    "f": set("aefg"),
    "_": set(),
}

_NORMAL_NODES = {
    "a": [
        (0.06, 0.95),
        (0.11, 1.0),
        (0.39, 1.0),
        (0.44, 0.95),
        (0.39, 0.9),
        (0.11, 0.9),
    ],
    "b": [
        (0.45, 0.94),
        (0.5, 0.89),
        (0.5, 0.56),
        (0.45, 0.51),
        (0.4, 0.56),
        (0.4, 0.89),
    ],
    "c": [
        (0.45, 0.49),
        (0.5, 0.44),
        (0.5, 0.11),
        (0.45, 0.06),
        (0.4, 0.11),
        (0.4, 0.44),
    ],
    "d": [
        (0.06, 0.05),
        (0.11, 0.1),
        (0.39, 0.1),
        (0.44, 0.05),
        (0.39, 0.0),
        (0.11, 0.0),
    ],
    "e": [
        (0.05, 0.49),
        (0.1, 0.44),
        (0.1, 0.11),
        (0.05, 0.06),
        (0.0, 0.11),
        (0.0, 0.44),
    ],
    "f": [
        (0.05, 0.94),
        (0.1, 0.89),
        (0.1, 0.56),
        (0.05, 0.51),
        (0.0, 0.56),
        (0.0, 0.89),
    ],
    "g": [
        (0.06, 0.5),
        (0.11, 0.55),
        (0.39, 0.55),
        (0.44, 0.5),
        (0.39, 0.45),
        (0.11, 0.45),
    ],
    "p": [
        (0.575, 0.1),
        (0.675, 0.1),
        (0.675, 0.0),
        (0.575, 0.0),
    ],
}

NODES_SET = {
    "normal": {k: [t.Vec2D(*p) for p in v] for k, v in _NORMAL_NODES.items()},
    "italic": {
        k: [t.Vec2D(0.2 * y + x, y) for x, y in v] for k, v in _NORMAL_NODES.items()
    },
}


class Mapper:
    """映射器类 (字符级别). 传入当前字符的左下角坐标和字体大小, 构建一个映射器对象."""

    def __init__(self, _start_pos: t.Vec2D, _fontsize: float = 72) -> None:
        self.start_pos = _start_pos
        self.fontsize = _fontsize

    def __call__(self, pos: t.Vec2D) -> t.Vec2D:
        """映射器对象的调用方法. 传入字符集的相对坐标, 返回实际绘制的坐标."""
        return pos * self.fontsize + self.start_pos


def args_check(
    digitals: str,
    align: str,
    font_name: str,
    refresh_level: _RLevel,
) -> None:
    """对最外层函数的四个关键参数进行合法性检查."""
    assert set(digitals) <= DISPLAY_CH | CTRL_CH | {"\n"}, "Invalid character in line"
    assert not re.search(
        f"^{CTRL_CH_RESTR}|{CTRL_CH_RESTR}{{2}}", digitals
    ), "pt (dot) myst behind a number (0-9, a-f, A-F) or a space (' ' or '_')"
    assert align in ("left", "center", "right"), "Invalid align"
    assert font_name in NODES_SET, "Invalid font style"
    assert refresh_level in (
        "digital",
        "line",
        "char",
        "path",
        None,
    ), "Invalid refresh level"


def len_line(line: str) -> int:
    """计算一行中实际显示的字符数 (因小数点不占位)."""
    return len(re.sub(CTRL_CH_RESTR, "", line))


def words_pos(
    pos: t.Vec2D,
    line: str,
    align: _Align,
    fontsize: float,
) -> List[t.Vec2D]:
    """计算一行中每个字符的起笔位置."""
    len_words = len_line(line)
    width = fontsize * 0.75
    if align == "left":
        return [pos + t.Vec2D(width * i, 0) for i in range(len_words + 1)]
    elif align == "center":
        return [
            pos + t.Vec2D(width * (i - len_words / 2), 0) for i in range(len_words + 1)
        ]
    elif align == "right":
        return [pos + t.Vec2D(width * (i - len_words), 0) for i in range(len_words + 1)]


if __name__ == "__main__":
    print(f"DISPLAY_CH = {DISPLAY_CH}")
    print(f"CTRL_CH = {CTRL_CH}")
    print(f"CHAR_SET = {CHAR_SET}")
    print(f"NODES_SET = {NODES_SET}")
