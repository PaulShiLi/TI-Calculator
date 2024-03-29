# Tokens from TI-Basic: Token dictionary from
# https://github.com/thenaterhood/basically-ti-basic/blob/master/src/basically_ti_basic/__main__.py

token = dict([
    (b'\x01', '>DMS'),
    (b'\x02', '>Dec'),
    (b'\x03', '>Frac'),
    (b'\x04', '→'),
    (b'\x05', 'BoxPlot'),
    (b'\x06', '['),
    (b'\x07', ']'),
    (b'\x08', '{'),
    (b'\x09', '}'),
    # (b'\x0A', 'r'),
    (b'\x0B', '°'),
    (b'\x0C', '^-1'),
    (b'\x0D', '^2'),
    (b'\x0E', '^T'),
    (b'\x0F', '^3'),
    (b'\x10', '('),
    (b'\x11', ')'),
    (b'\x12', 'round('),
    (b'\x13', 'pxl-Test('),
    (b'\x14', 'augment('),
    (b'\x15', 'rowSwap('),
    (b'\x16', 'row+('),
    (b'\x17', '*row('),
    (b'\x18', '*row+('),
    (b'\x19', 'max('),
    (b'\x1A', 'min('),
    (b'\x1B', 'R>Pr('),
    (b'\x1C', 'R>P[theta]('),
    (b'\x1D', 'P>Rx('),
    (b'\x1E', 'P>Ry('),
    (b'\x1F', 'median('),
    (b'\x20', 'randM('),
    (b'\x21', 'mean('),
    (b'\x22', 'solve('),
    (b'\x23', 'seq('),
    (b'\x24', 'fnInt('),
    (b'\x25', 'nDeriv('),
    # Unknown function
    # (b'\x26', ''),
    (b'\x27', 'fMin('),
    (b'\x28', 'fMax('),
    (b'\x29', ' '),
    (b'\x2A', '"'),
    (b'\x2B', ','),
    (b'\x2C', 'imaginary'),
    (b'\x2D', '!'),
    (b'\x2E', 'CubicReg '),
    (b'\x2F', 'QuartReg '),
    (b'\x3A', '.'),
    (b'\x3B', '10^'),
    (b'\x3C', ' or '),
    (b'\x3D', ' xor '),
    (b'\x3E', ':'),
    (b'\x3F', '\n'),
    (b'\x40', ' and '),
    (b'\x41', 'A'),
    (b'\x42', 'B'),
    (b'\x43', 'C'),
    (b'\x44', 'D'),
    (b'\x45', 'E'),
    (b'\x46', 'F'),
    (b'\x47', 'G'),
    (b'\x48', 'H'),
    (b'\x49', 'I'),
    (b'\x4A', 'J'),
    (b'\x4B', 'K'),
    (b'\x4C', 'L'),
    (b'\x4D', 'M'),
    (b'\x4E', 'N'),
    (b'\x4F', 'O'),
    (b'\x50', 'P'),
    (b'\x51', 'Q'),
    (b'\x52', 'R'),
    (b'\x53', 'S'),
    (b'\x54', 'T'),
    (b'\x55', 'U'),
    (b'\x56', 'V'),
    (b'\x57', 'W'),
    (b'\x58', 'X'),
    (b'\x59', 'Y'),
    (b'\x5A', 'Z'),
    (b'\x30', '0'),
    (b'\x31', '1'),
    (b'\x32', '2'),
    (b'\x33', '3'),
    (b'\x34', '4'),
    (b'\x35', '5'),
    (b'\x36', '6'),
    (b'\x37', '7'),
    (b'\x38', '8'),
    (b'\x39', '9'),
    (b'\x5B', '[theta]'),
    (b'\x5C\x00', '[A]'),
    (b'\x5C\x01', '[B]'),
    (b'\x5C\x02', '[C]'),
    (b'\x5C\x03', '[D]'),
    (b'\x5C\x04', '[E]'),
    (b'\x5C\x05', '[F]'),
    (b'\x5C\x06', '[G]'),
    (b'\x5C\x07', '[H]'),
    (b'\x5C\x08', '[I]'),
    (b'\x5C\x09', '[J]'),
    (b'\x5D\x00', 'l1'),
    (b'\x5D\x01', 'l2'),
    (b'\x5D\x02', 'l3'),
    (b'\x5D\x03', 'l4'),
    (b'\x5D\x04', 'l5'),
    (b'\x5D\x05', 'l6'),
    (b'\x5D\x06', 'l7'),
    (b'\x5D\x07', 'l8'),
    (b'\x5D\x08', 'l0'),
    (b'\x5E\x10', 'y1'),
    (b'\x5E\x11', 'y2'),
    (b'\x5E\x12', 'y3'),
    (b'\x5E\x13', 'y4'),
    (b'\x5E\x14', 'y5'),
    (b'\x5E\x15', 'y6'),
    (b'\x5E\x16', 'y7'),
    (b'\x5E\x17', 'y8'),
    (b'\x5E\x18', 'y9'),
    (b'\x5E\x19', 'y0'),
    (b'\x5E\x40', 'r_1'),
    (b'\x5E\x41', 'r_2'),
    (b'\x5E\x42', 'r_3'),
    (b'\x5E\x43', 'r_4'),
    (b'\x5E\x44', 'r_5'),
    (b'\x5E\x45', 'r_6'),
    (b'\x5E\x20', 'x1t'),
    (b'\x5E\x21', 'y1t'),
    (b'\x5E\x22', 'x2t'),
    (b'\x5E\x23', 'y2t'),
    (b'\x5E\x24', 'x3t'),
    (b'\x5E\x25', 'y3t'),
    (b'\x5E\x26', 'x4t'),
    (b'\x5E\x27', 'y4t'),
    (b'\x5E\x28', 'x5t'),
    (b'\x5E\x29', 'y5t'),
    (b'\x5E\x2A', 'x6t'),
    (b'\x5E\x2B', 'y6t'),
    (b'\x5F', 'prgm'),
    (b'\x60\x00', 'Pic1'),
    (b'\x60\x01', 'Pic2'),
    (b'\x60\x02', 'Pic3'),
    (b'\x60\x03', 'Pic4'),
    (b'\x60\x04', 'Pic5'),
    (b'\x60\x05', 'Pic6'),
    (b'\x60\x06', 'Pic7'),
    (b'\x60\x07', 'Pic8'),
    (b'\x60\x08', 'Pic9'),
    (b'\x60\x09', 'Pic0'),
    (b'\x61\x00', 'GDB1'),
    (b'\x61\x01', 'GDB2'),
    (b'\x61\x02', 'GDB3'),
    (b'\x61\x03', 'GDB4'),
    (b'\x61\x04', 'GDB5'),
    (b'\x61\x05', 'GDB6'),
    (b'\x61\x06', 'GDB7'),
    (b'\x61\x07', 'GDB8'),
    (b'\x61\x08', 'GDB9'),
    (b'\x61\x09', 'GDB0'),
    # Unknown
    # (b'\x62\x00', ''),
    (b'\x62\x01', 'RegEq'),
    # Unsupported for now, will break parsing
    # (b'\x62\x02', 'n'),
    (b'\x62\x03', '[x-bar]'),
    (b'\x62\x04', '[Summ x]'),
    (b'\x62\x05', '[Summ x^2]'),
    (b'\x62\x06', 'Sx'),
    (b'\x62\x07', '[sigma]x'),
    (b'\x62\x08', 'minX'),
    (b'\x62\x09', 'maxX'),
    (b'\x62\x0A', 'minY'),
    (b'\x62\x0B', 'maxY'),
    (b'\x62\x0C', '[y-bar]'),
    (b'\x62\x0D', '[Summ y]'),
    (b'\x62\x0E', '[Summ y^2]'),
    (b'\x62\x0F', 'Sy'),
    (b'\x62\x10', '[sigma]y'),
    (b'\x62\x11', '[Summ xy]'),
    # Unsupported as-is, will break re-compiling
    # (b'\x62\x12', 'r'),
    (b'\x62\x13', 'Med'),
    (b'\x62\x14', 'Q1'),
    (b'\x62\x15', 'Q3'),
    # Unsupported as-is, will break re-compiling
    # (b'\x62\x16', 'a'),
    # (b'\x62\x17', 'b'),
    # (b'\x62\x18', 'c'),
    # (b'\x62\x19', 'd'),
    # (b'\x62\x1A', 'e'),
    (b'\x62\x1B', 'x1'),
    (b'\x62\x1C', 'x2'),
    (b'\x62\x1D', 'x3'),
    (b'\x62\x1E', 'y1'),
    (b'\x62\x1F', 'y2'),
    (b'\x62\x20', 'y3'),
    (b'\x62\x25', '[chi]2'),
    (b'\x62\x26', '[fin]'),
    (b'\x62\x27', 'df'),
    (b'\x62\x28', '[p-hat]'),
    (b'\x62\x29', '[p-hat]1'),
    (b'\x62\x2A', '[p-hat]2'),
    (b'\x62\x2B', '[x-bar]1'),
    (b'\x62\x2C', 'Sx1'),
    (b'\x62\x2D', 'n_1'),
    (b'\x62\x2E', '[x-bar]2'),
    (b'\x62\x2F', 'Sx2'),
    (b'\x62\x30', 'n_2'),
    (b'\x62\x31', 'Sxp'),
    (b'\x62\x32', 'lower'),
    (b'\x62\x33', 'upper'),
    # Unsupported as-is, will break re-compiling
    # (b'\x62\x34', 's'),
    (b'\x62\x35', 'r2'),
    (b'\x62\x36', 'R2'),
    # This may be a duplicate of the df above
    # (b'\x62\x37', 'df'),
    (b'\x62\x38', 'SS'),
    (b'\x62\x39', 'MS'),
    # More potential duplicates
    # (b'\x62\x3A', 'df'),
    # (b'\x62\x3B', 'SS'),
    # (b'\x62\x3C', 'MS'),
    (b'\x63\x00', 'ZXscl'),
    (b'\x63\x01', 'ZYscl'),
    (b'\x63\x02', 'Xscl'),
    (b'\x63\x03', 'Yscl'),
    (b'\x63\x04', 'U_nStart'),
    (b'\x63\x05', 'V_nStart'),
    (b'\x63\x06', 'U_(n-1)'),
    (b'\x63\x07', 'V_(n-1)'),
    # \x63\xx values are not complete
    (b'\x64', 'Radian'),
    (b'\x65', 'Degree'),
    (b'\x66', 'Normal'),
    (b'\x67', 'Sci'),
    (b'\x68', 'Eng'),
    (b'\x69', 'Float'),
    (b'\x6A', '='),
    (b'\x6B', '<'),
    (b'\x6C', '>'),
    (b'\x6D', '<='),
    (b'\x6E', '>='),
    (b'\x6F', '!='),
    (b'\x70', '+'),
    (b'\x71', '–'),
    (b'\x72', 'Ans'),
    (b'\x73', 'Fix '),
    (b'\x74', 'Horiz'),
    (b'\x75', 'Full'),
    (b'\x76', 'Func'),
    (b'\x77', 'Param'),
    (b'\x78', 'Polar'),
    (b'\x79', 'Seq'),
    (b'\x7A', 'IndpntAuto'),
    (b'\x7B', 'IndpntAsk'),
    (b'\x7C', 'DependAuto'),
    (b'\x7D', 'DependAsk'),
    # 73 ** (Graph Options)
    (b'\x7E\x00', 'Sequential'),
    (b'\x7E\x01', 'Simul'),
    (b'\x7E\x02', 'PolarGC'),
    (b'\x7E\x03', 'RectGC'),
    (b'\x7E\x04', 'CoordOn'),
    (b'\x7E\x05', 'CoordOff'),
    (b'\x7E\x06', 'Connected'),
    (b'\x7E\x07', 'Dot'),
    (b'\x7E\x08', 'AxesOn'),
    (b'\x7E\x09', 'AxesOff'),
    (b'\x7E\x0A', 'GridOn'),
    (b'\x7E\x0B', 'GridOff'),
    (b'\x7E\x0C', 'LabelOn'),
    (b'\x7E\x0D', 'LabelOff'),
    (b'\x7E\x0E', 'Web'),
    (b'\x7E\x0F', 'Time'),
    (b'\x7E\x10', 'uvAxes'),
    (b'\x7E\x11', 'vwAxes'),
    (b'\x7E\x12', 'uwAxes'),
    # End of 7E Options
    (b'\x7F', '[box]'),
    (b'\x80', '[cross]'),
    (b'\x81', '[dot]'),
    (b'\x82', '*'),
    (b'\x83', '/'),
    (b'\x84', 'Trace'),
    (b'\x85', 'ClrDraw'),
    (b'\x86', 'ZStandard'),
    (b'\x87', 'ZTrig'),
    (b'\x88', 'ZBox'),
    (b'\x89', 'Zoom_In'),
    (b'\x8A', 'Zoom_Out'),
    (b'\x8B', 'ZSquare'),
    (b'\x8C', 'ZInteger'),
    (b'\x8D', 'ZPrevious'),
    (b'\x8E', 'ZDecimal'),
    (b'\x8F', 'ZoomStat'),
    (b'\x90', 'ZoomRcl'),
    (b'\x91', 'PrintScreen'),
    (b'\x92', 'ZoomSto'),
    (b'\x93', 'Text('),
    (b'\x94', ' nPr '),
    (b'\x95', ' nCr '),
    (b'\x96', 'FnOn '),
    (b'\x97', 'FnOff '),
    (b'\x98', 'StorePic '),
    (b'\x99', 'RecallPic '),
    (b'\x9A', 'StoreGDB '),
    (b'\x9B', 'RecallGDB '),
    (b'\x9C', 'Line('),
    (b'\x9D', 'Vertical '),
    (b'\x9E', 'Pt-On('),
    (b'\x9F', 'Pt-Off('),
    (b'\xA0', 'Pt-Change( '),
    (b'\xA1', 'Pxl-On( '),
    (b'\xA2', 'Pxl-Off( '),
    (b'\xA3', 'Pxl-Change( '),
    (b'\xA4', 'Shade('),
    (b'\xA5', 'Circle('),
    (b'\xA6', 'Horizontal '),
    (b'\xA7', 'Tangent('),
    (b'\xA8', 'DrawInv '),
    (b'\xA9', 'DrawF '),
    # System variables (TODO)
    (b'\xAA\x00', 'Str1'),
    (b'\xAA\x01', 'Str2'),
    (b'\xAA\x02', 'Str3'),
    (b'\xAA\x03', 'Str4'),
    (b'\xAA\x04', 'Str5'),
    (b'\xAA\x05', 'Str6'),
    (b'\xAA\x06', 'Str7'),
    (b'\xAA\x07', 'Str8'),
    (b'\xAA\x08', 'Str9'),
    (b'\xAA\x09', 'Str0'),
    (b'\xAB', 'rand'),
    (b'\xAC', '[pi]'),
    (b'\xAD', 'getKey'),
    (b'\xAE', '\''),
    (b'\xAF', '?'),
    (b'\xB0', '-'),
    (b'\xB1', 'int('),
    (b'\xB2', 'abs('),
    (b'\xB3', 'det('),
    (b'\xB4', 'identity('),
    (b'\xB5', 'dim('),
    (b'\xB6', 'sum('),
    (b'\xB7', 'prod('),
    (b'\xB8', 'not('),
    (b'\xB9', 'iPart('),
    (b'\xBA', 'fPart('),
    # BB tokens (two-byte), Incomplete TODO
    (b'\xBB\x00', 'npv('),
    (b'\xBB\x01', 'irr('),
    (b'\xBB\x02', 'bal('),
    (b'\xBB\x03', 'SummPrn('),
    (b'\xBB\x04', 'SummInt('),
    (b'\xBB\x05', '>Nom('),
    (b'\xBB\x06', '>Eff('),
    (b'\xBB\x07', 'dbd('),
    (b'\xBB\x08', 'lcm('),
    (b'\xBB\x09', 'gcd('),
    (b'\xBB\x25', 'conj('),
    (b'\xBB\x26', 'real('),
    (b'\xBB\x27', 'imag('),
    (b'\xBB\x0A', 'randInt('),
    (b'\xBB\x0B', 'randBin('),
    (b'\xBB\x0C', 'sub('),
    (b'\xBB\x0D', 'stdDev('),
    (b'\xBB\x0E', 'variance('),
    (b'\xBB\x0F', 'inString('),
    (b'\xBB\xB0', 'a'),
    (b'\xBB\xB1', 'b'),
    (b'\xBB\xB2', 'c'),
    (b'\xBB\xB3', 'd'),
    (b'\xBB\xB4', 'e'),
    (b'\xBB\xB5', 'f'),
    (b'\xBB\xB6', 'g'),
    (b'\xBB\xB7', 'h'),
    (b'\xBB\xB8', 'i'),
    (b'\xBB\xB9', 'j'),
    (b'\xBB\xBA', 'k'),
    (b'\xBB\xBC', 'l'),
    (b'\xBB\xBD', 'm'),
    (b'\xBB\xBE', 'n'),
    (b'\xBB\xBF', 'o'),
    (b'\xBB\xC0', 'p'),
    (b'\xBB\xC1', 'q'),
    (b'\xBB\xC2', 'r'),
    (b'\xBB\xC3', 's'),
    (b'\xBB\xC4', 't'),
    (b'\xBB\xC5', 'u'),
    (b'\xBB\xC6', 'v'),
    (b'\xBB\xC7', 'w'),
    (b'\xBB\xC8', 'x'),
    (b'\xBB\xC9', 'y'),
    (b'\xBB\xCA', 'z'),
    (b'\xBB\xF1', 'randNorm('),
    # end of xBB
    (b'\xBC', 'sqrt('),
    (b'\xBD', 'cubrt('),
    (b'\xBE', 'ln ('),
    (b'\xBF', 'e^('),
    (b'\xC0', 'log('),
    (b'\xC1', '10^('),
    (b'\xC2', 'sin('),
    (b'\xC3', 'sin^-1('),
    (b'\xC4', 'cos('),
    (b'\xC5', 'cos^-1('),
    (b'\xC6', 'tan('),
    (b'\xC7', 'tan^-1('),
    (b'\xC8', 'sinh('),
    (b'\xC9', 'sinh^-1('),
    (b'\xCA', 'cosh('),
    (b'\xCB', 'cosh^-1('),
    (b'\xCC', 'tanh('),
    (b'\xCD', 'tanh^-1('),
    (b'\xCE', 'If '),
    (b'\xCF', 'Then'),
    (b'\xD0', 'Else'),
    (b'\xD1', 'While '),
    (b'\xD2', 'Repeat '),
    (b'\xD3', 'For '),
    (b'\xD4', 'End'),
    (b'\xD5', 'Return'),
    (b'\xD6', 'Lbl '),
    (b'\xD7', 'Goto '),
    (b'\xD8', 'Pause '),
    (b'\xD9', 'Stop'),
    (b'\xDA', 'IS>('),
    (b'\xDB', 'DS>('),
    (b'\xDC', 'Input '),
    (b'\xDD', 'Prompt '),
    (b'\xDE', 'Disp '),
    (b'\xDF', 'DispGraph'),
    (b'\xE0', 'Output('),
    (b'\xE1', 'ClrHome'),
    (b'\xE2', 'Fill('),
    (b'\xE3', 'SortA('),
    (b'\xE4', 'SortD('),
    (b'\xE5', 'DispTable'),
    (b'\xE6', 'Menu('),
    (b'\xE7', 'Send('),
    (b'\xE8', 'Get('),
    (b'\xE9', 'PlotsOn '),
    (b'\xEA', 'PlotsOff '),
    # No idea what this operator is, so we're not supporting it until I
    # know how it fits in things so encoding don't break with it
    # (b'\xEB', 'L'),
    (b'\xEC', 'Plot1('),
    (b'\xED', 'Plot2('),
    (b'\xEE', 'Plot3('),
    # Unknown
    # (b'\xEF', ''),
    (b'\xF0', '^'),
    (b'\xF1', '[xth root]'),
    (b'\xF2', '1-Var Stats '),
    (b'\xF3', '2-Var Stats '),
    (b'\xF4', 'LinReg(a+bx) '),
    (b'\xF5', 'ExpReg '),
    (b'\xF6', 'LnReg '),
    (b'\xF7', 'PwrReg '),
    (b'\xF8', 'Med-Med '),
    (b'\xF9', 'QuadReg '),
    (b'\xFA', 'ClrList '),
    (b'\xFB', 'ClrTable'),
    (b'\xFC', 'Histogram'),
    (b'\xFD', 'xyLine'),
    (b'\xFE', 'Scatter'),
    (b'\xFF', 'LinReg(ax+b) '),
])

invToken = {v: k for k, v in token.items()}
strToken = {rf"{k}".replace("b", "").replace("'", ""): v for k, v in token.items() if type(k) == bytes}


class tokens:
    token = token
    invToken = invToken

    def fetchTByte(token: str):
        token = str(token)
        try:
            return invToken[token]
        except Exception as e:
            return f"Perhaps you mean {[key for key in invToken.keys() if token in str(key)]} caused by error: {e}"

    def fetchToken(byte: bytes):
        try:
            return token[byte]
        except Exception as e:
            return e
