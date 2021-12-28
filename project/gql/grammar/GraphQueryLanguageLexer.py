# Generated from ./project/gql/grammar/GraphQueryLanguage.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u01ee\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\5\2g\n\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\5\2n\n\2\3\3\5\3q\n\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3y\n\3\3\4\5\4|\n\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u0083\n\4\3\5\5\5\u0086\n\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u008d\n\5\3\6\5\6\u0090\n\6\3\6\3\6\3\6\3\6\5\6\u0096")
        buf.write("\n\6\3\7\5\7\u0099\n\7\3\7\3\7\3\7\3\7\5\7\u009f\n\7\3")
        buf.write("\b\5\b\u00a2\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u00ae\n\b\3\t\5\t\u00b1\n\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u00bb\n\t\3\n\5\n\u00be\n\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\5\n\u00c8\n\n\3\13\5\13\u00cb\n")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00d4\n\13")
        buf.write("\3\f\5\f\u00d7\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00e4\n\f\3\r\5\r\u00e7\n\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00f0\n\r\3\16\5\16\u00f3\n\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00fc\n\16\3\17\5")
        buf.write("\17\u00ff\n\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0107")
        buf.write("\n\17\3\20\5\20\u010a\n\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\5\20\u0114\n\20\3\21\5\21\u0117\n\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u011e\n\21\3\22\5\22\u0121\n")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u012a\n\22")
        buf.write("\3\23\3\23\5\23\u012e\n\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\26\5\26\u013c\n\26\3\26")
        buf.write("\3\26\5\26\u0140\n\26\3\27\5\27\u0143\n\27\3\27\3\27\5")
        buf.write("\27\u0147\n\27\3\30\5\30\u014a\n\30\3\30\3\30\5\30\u014e")
        buf.write("\n\30\3\31\5\31\u0151\n\31\3\31\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u0158\n\31\3\32\5\32\u015b\n\32\3\32\3\32\3\32\3\32")
        buf.write("\5\32\u0161\n\32\3\33\5\33\u0164\n\33\3\33\3\33\5\33\u0168")
        buf.write("\n\33\3\34\5\34\u016b\n\34\3\34\3\34\5\34\u016f\n\34\3")
        buf.write("\35\5\35\u0172\n\35\3\35\3\35\5\35\u0176\n\35\3\36\3\36")
        buf.write("\5\36\u017a\n\36\3\37\3\37\5\37\u017e\n\37\3 \5 \u0181")
        buf.write("\n \3 \3 \5 \u0185\n \3!\3!\5!\u0189\n!\3\"\5\"\u018c")
        buf.write("\n\"\3\"\3\"\5\"\u0190\n\"\3#\3#\3$\3$\3$\3$\3%\3%\3&")
        buf.write("\3&\3&\3\'\3\'\3\'\3(\3(\5(\u01a2\n(\3(\7(\u01a5\n(\f")
        buf.write("(\16(\u01a8\13(\3)\3)\7)\u01ac\n)\f)\16)\u01af\13)\3)")
        buf.write("\5)\u01b2\n)\3*\3*\3*\3*\3*\7*\u01b9\n*\f*\16*\u01bc\13")
        buf.write("*\3*\3*\3+\3+\3+\3+\7+\u01c4\n+\f+\16+\u01c7\13+\3+\3")
        buf.write("+\3,\3,\3,\3,\3,\7,\u01d0\n,\f,\16,\u01d3\13,\3,\3,\3")
        buf.write("-\3-\3-\5-\u01da\n-\3.\5.\u01dd\n.\3/\3/\3\60\3\60\3\61")
        buf.write("\6\61\u01e4\n\61\r\61\16\61\u01e5\3\61\3\61\3\62\6\62")
        buf.write("\u01eb\n\62\r\62\16\62\u01ec\2\2\63\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63\3\2\n\4\2\f\f\"\"\4\2\"\"aa\6\2\"\"\61\61")
        buf.write("^^aa\4\2C\\c|\3\2\63;\3\2\62;\5\2\13\13\17\17\"\"\3\2")
        buf.write("\f\f\2\u023a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\3f")
        buf.write("\3\2\2\2\5p\3\2\2\2\7{\3\2\2\2\t\u0085\3\2\2\2\13\u008f")
        buf.write("\3\2\2\2\r\u0098\3\2\2\2\17\u00a1\3\2\2\2\21\u00b0\3\2")
        buf.write("\2\2\23\u00bd\3\2\2\2\25\u00ca\3\2\2\2\27\u00d6\3\2\2")
        buf.write("\2\31\u00e6\3\2\2\2\33\u00f2\3\2\2\2\35\u00fe\3\2\2\2")
        buf.write("\37\u0109\3\2\2\2!\u0116\3\2\2\2#\u0120\3\2\2\2%\u012d")
        buf.write("\3\2\2\2\'\u012f\3\2\2\2)\u0134\3\2\2\2+\u013b\3\2\2\2")
        buf.write("-\u0142\3\2\2\2/\u0149\3\2\2\2\61\u0150\3\2\2\2\63\u015a")
        buf.write("\3\2\2\2\65\u0163\3\2\2\2\67\u016a\3\2\2\29\u0171\3\2")
        buf.write("\2\2;\u0177\3\2\2\2=\u017b\3\2\2\2?\u0180\3\2\2\2A\u0186")
        buf.write("\3\2\2\2C\u018b\3\2\2\2E\u0191\3\2\2\2G\u0193\3\2\2\2")
        buf.write("I\u0197\3\2\2\2K\u0199\3\2\2\2M\u019c\3\2\2\2O\u01a1\3")
        buf.write("\2\2\2Q\u01b1\3\2\2\2S\u01b3\3\2\2\2U\u01bf\3\2\2\2W\u01ca")
        buf.write("\3\2\2\2Y\u01d9\3\2\2\2[\u01dc\3\2\2\2]\u01de\3\2\2\2")
        buf.write("_\u01e0\3\2\2\2a\u01e3\3\2\2\2c\u01ea\3\2\2\2eg\5a\61")
        buf.write("\2fe\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\7H\2\2ij\7W\2\2jk\7")
        buf.write("P\2\2km\3\2\2\2ln\5a\61\2ml\3\2\2\2mn\3\2\2\2n\4\3\2\2")
        buf.write("\2oq\5a\61\2po\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\7N\2\2st")
        buf.write("\7Q\2\2tu\7C\2\2uv\7F\2\2vx\3\2\2\2wy\5a\61\2xw\3\2\2")
        buf.write("\2xy\3\2\2\2y\6\3\2\2\2z|\5a\61\2{z\3\2\2\2{|\3\2\2\2")
        buf.write("|}\3\2\2\2}~\7U\2\2~\177\7G\2\2\177\u0080\7V\2\2\u0080")
        buf.write("\u0082\3\2\2\2\u0081\u0083\5a\61\2\u0082\u0081\3\2\2\2")
        buf.write("\u0082\u0083\3\2\2\2\u0083\b\3\2\2\2\u0084\u0086\5a\61")
        buf.write("\2\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\u0088\7C\2\2\u0088\u0089\7F\2\2\u0089\u008a")
        buf.write("\7F\2\2\u008a\u008c\3\2\2\2\u008b\u008d\5a\61\2\u008c")
        buf.write("\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d\n\3\2\2\2\u008e")
        buf.write("\u0090\5a\61\2\u008f\u008e\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u0092\7Q\2\2\u0092\u0093\7")
        buf.write("H\2\2\u0093\u0095\3\2\2\2\u0094\u0096\5a\61\2\u0095\u0094")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\f\3\2\2\2\u0097\u0099")
        buf.write("\5a\61\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u009b\7V\2\2\u009b\u009c\7Q\2\2\u009c")
        buf.write("\u009e\3\2\2\2\u009d\u009f\5a\61\2\u009e\u009d\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\16\3\2\2\2\u00a0\u00a2\5a\61")
        buf.write("\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a4\7X\2\2\u00a4\u00a5\7G\2\2\u00a5\u00a6")
        buf.write("\7T\2\2\u00a6\u00a7\7V\2\2\u00a7\u00a8\7K\2\2\u00a8\u00a9")
        buf.write("\7E\2\2\u00a9\u00aa\7G\2\2\u00aa\u00ab\7U\2\2\u00ab\u00ad")
        buf.write("\3\2\2\2\u00ac\u00ae\5a\61\2\u00ad\u00ac\3\2\2\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ae\20\3\2\2\2\u00af\u00b1\5a\61\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2\u00b3\7N\2\2\u00b3\u00b4\7C\2\2\u00b4\u00b5\7D")
        buf.write("\2\2\u00b5\u00b6\7G\2\2\u00b6\u00b7\7N\2\2\u00b7\u00b8")
        buf.write("\7U\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00bb\5a\61\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\22\3\2\2\2\u00bc")
        buf.write("\u00be\5a\61\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\u00c0\7U\2\2\u00c0\u00c1\7")
        buf.write("G\2\2\u00c1\u00c2\7N\2\2\u00c2\u00c3\7G\2\2\u00c3\u00c4")
        buf.write("\7E\2\2\u00c4\u00c5\7V\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c8")
        buf.write("\5a\61\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\24\3\2\2\2\u00c9\u00cb\5a\61\2\u00ca\u00c9\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\7G\2\2")
        buf.write("\u00cd\u00ce\7F\2\2\u00ce\u00cf\7I\2\2\u00cf\u00d0\7G")
        buf.write("\2\2\u00d0\u00d1\7U\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00d4")
        buf.write("\5a\61\2\u00d3\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\26\3\2\2\2\u00d5\u00d7\5a\61\2\u00d6\u00d5\3\2\2\2\u00d6")
        buf.write("\u00d7\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\7T\2\2")
        buf.write("\u00d9\u00da\7G\2\2\u00da\u00db\7C\2\2\u00db\u00dc\7E")
        buf.write("\2\2\u00dc\u00dd\7J\2\2\u00dd\u00de\7C\2\2\u00de\u00df")
        buf.write("\7D\2\2\u00df\u00e0\7N\2\2\u00e0\u00e1\7G\2\2\u00e1\u00e3")
        buf.write("\3\2\2\2\u00e2\u00e4\5a\61\2\u00e3\u00e2\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\30\3\2\2\2\u00e5\u00e7\5a\61\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\7U\2\2\u00e9\u00ea\7V\2\2\u00ea\u00eb\7C")
        buf.write("\2\2\u00eb\u00ec\7T\2\2\u00ec\u00ed\7V\2\2\u00ed\u00ef")
        buf.write("\3\2\2\2\u00ee\u00f0\5a\61\2\u00ef\u00ee\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\32\3\2\2\2\u00f1\u00f3\5a\61\2\u00f2")
        buf.write("\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\3\2\2\2")
        buf.write("\u00f4\u00f5\7H\2\2\u00f5\u00f6\7K\2\2\u00f6\u00f7\7P")
        buf.write("\2\2\u00f7\u00f8\7C\2\2\u00f8\u00f9\7N\2\2\u00f9\u00fb")
        buf.write("\3\2\2\2\u00fa\u00fc\5a\61\2\u00fb\u00fa\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\34\3\2\2\2\u00fd\u00ff\5a\61\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u0100\u0101\7H\2\2\u0101\u0102\7T\2\2\u0102\u0103\7Q")
        buf.write("\2\2\u0103\u0104\7O\2\2\u0104\u0106\3\2\2\2\u0105\u0107")
        buf.write("\5a\61\2\u0106\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107")
        buf.write("\36\3\2\2\2\u0108\u010a\5a\61\2\u0109\u0108\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c\7H\2\2")
        buf.write("\u010c\u010d\7K\2\2\u010d\u010e\7N\2\2\u010e\u010f\7V")
        buf.write("\2\2\u010f\u0110\7G\2\2\u0110\u0111\7T\2\2\u0111\u0113")
        buf.write("\3\2\2\2\u0112\u0114\5a\61\2\u0113\u0112\3\2\2\2\u0113")
        buf.write("\u0114\3\2\2\2\u0114 \3\2\2\2\u0115\u0117\5a\61\2\u0116")
        buf.write("\u0115\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\3\2\2\2")
        buf.write("\u0118\u0119\7O\2\2\u0119\u011a\7C\2\2\u011a\u011b\7R")
        buf.write("\2\2\u011b\u011d\3\2\2\2\u011c\u011e\5a\61\2\u011d\u011c")
        buf.write("\3\2\2\2\u011d\u011e\3\2\2\2\u011e\"\3\2\2\2\u011f\u0121")
        buf.write("\5a\61\2\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0123\7R\2\2\u0123\u0124\7T\2\2\u0124")
        buf.write("\u0125\7K\2\2\u0125\u0126\7P\2\2\u0126\u0127\7V\2\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u012a\5a\61\2\u0129\u0128\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a$\3\2\2\2\u012b\u012e\5\'\24")
        buf.write("\2\u012c\u012e\5)\25\2\u012d\u012b\3\2\2\2\u012d\u012c")
        buf.write("\3\2\2\2\u012e&\3\2\2\2\u012f\u0130\7V\2\2\u0130\u0131")
        buf.write("\7T\2\2\u0131\u0132\7W\2\2\u0132\u0133\7G\2\2\u0133(\3")
        buf.write("\2\2\2\u0134\u0135\7H\2\2\u0135\u0136\7C\2\2\u0136\u0137")
        buf.write("\7N\2\2\u0137\u0138\7U\2\2\u0138\u0139\7G\2\2\u0139*\3")
        buf.write("\2\2\2\u013a\u013c\5a\61\2\u013b\u013a\3\2\2\2\u013b\u013c")
        buf.write("\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013f\7?\2\2\u013e")
        buf.write("\u0140\5a\61\2\u013f\u013e\3\2\2\2\u013f\u0140\3\2\2\2")
        buf.write("\u0140,\3\2\2\2\u0141\u0143\5a\61\2\u0142\u0141\3\2\2")
        buf.write("\2\u0142\u0143\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0146")
        buf.write("\7(\2\2\u0145\u0147\5a\61\2\u0146\u0145\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147.\3\2\2\2\u0148\u014a\5a\61\2\u0149")
        buf.write("\u0148\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014b\u014d\7~\2\2\u014c\u014e\5a\61\2\u014d\u014c\3")
        buf.write("\2\2\2\u014d\u014e\3\2\2\2\u014e\60\3\2\2\2\u014f\u0151")
        buf.write("\5a\61\2\u0150\u014f\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\u0153\7P\2\2\u0153\u0154\7Q\2\2\u0154")
        buf.write("\u0155\7V\2\2\u0155\u0157\3\2\2\2\u0156\u0158\5a\61\2")
        buf.write("\u0157\u0156\3\2\2\2\u0157\u0158\3\2\2\2\u0158\62\3\2")
        buf.write("\2\2\u0159\u015b\5a\61\2\u015a\u0159\3\2\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\7K\2\2\u015d")
        buf.write("\u015e\7P\2\2\u015e\u0160\3\2\2\2\u015f\u0161\5a\61\2")
        buf.write("\u0160\u015f\3\2\2\2\u0160\u0161\3\2\2\2\u0161\64\3\2")
        buf.write("\2\2\u0162\u0164\5a\61\2\u0163\u0162\3\2\2\2\u0163\u0164")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\7,\2\2\u0166")
        buf.write("\u0168\5a\61\2\u0167\u0166\3\2\2\2\u0167\u0168\3\2\2\2")
        buf.write("\u0168\66\3\2\2\2\u0169\u016b\5a\61\2\u016a\u0169\3\2")
        buf.write("\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016e")
        buf.write("\7\60\2\2\u016d\u016f\5a\61\2\u016e\u016d\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f8\3\2\2\2\u0170\u0172\5a\61\2\u0171")
        buf.write("\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0175\7.\2\2\u0174\u0176\5a\61\2\u0175\u0174\3")
        buf.write("\2\2\2\u0175\u0176\3\2\2\2\u0176:\3\2\2\2\u0177\u0179")
        buf.write("\7=\2\2\u0178\u017a\5a\61\2\u0179\u0178\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a<\3\2\2\2\u017b\u017d\7}\2\2\u017c")
        buf.write("\u017e\5a\61\2\u017d\u017c\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e>\3\2\2\2\u017f\u0181\5a\61\2\u0180\u017f\3\2\2")
        buf.write("\2\u0180\u0181\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0184")
        buf.write("\7\177\2\2\u0183\u0185\5a\61\2\u0184\u0183\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185@\3\2\2\2\u0186\u0188\7*\2\2\u0187")
        buf.write("\u0189\5a\61\2\u0188\u0187\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189B\3\2\2\2\u018a\u018c\5a\61\2\u018b\u018a\3\2\2")
        buf.write("\2\u018b\u018c\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f")
        buf.write("\7+\2\2\u018e\u0190\5a\61\2\u018f\u018e\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190D\3\2\2\2\u0191\u0192\7$\2\2\u0192")
        buf.write("F\3\2\2\2\u0193\u0194\7$\2\2\u0194\u0195\7$\2\2\u0195")
        buf.write("\u0196\7$\2\2\u0196H\3\2\2\2\u0197\u0198\7<\2\2\u0198")
        buf.write("J\3\2\2\2\u0199\u019a\7?\2\2\u019a\u019b\7@\2\2\u019b")
        buf.write("L\3\2\2\2\u019c\u019d\7/\2\2\u019d\u019e\7@\2\2\u019e")
        buf.write("N\3\2\2\2\u019f\u01a2\7a\2\2\u01a0\u01a2\5[.\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a6\3\2\2\2\u01a3")
        buf.write("\u01a5\5Y-\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7P\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a9\u01ad\5]/\2\u01aa\u01ac\5_\60\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01b2\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01b0\u01b2\7\62\2\2\u01b1\u01a9\3\2\2\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2R\3\2\2\2\u01b3\u01ba\5G$\2\u01b4")
        buf.write("\u01b9\5[.\2\u01b5\u01b9\5_\60\2\u01b6\u01b9\t\2\2\2\u01b7")
        buf.write("\u01b9\5M\'\2\u01b8\u01b4\3\2\2\2\u01b8\u01b5\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc\3")
        buf.write("\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd")
        buf.write("\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be\5G$\2\u01beT")
        buf.write("\3\2\2\2\u01bf\u01c5\5E#\2\u01c0\u01c4\5[.\2\u01c1\u01c4")
        buf.write("\5_\60\2\u01c2\u01c4\t\3\2\2\u01c3\u01c0\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c8\3")
        buf.write("\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c9\5E#\2\u01c9V\3")
        buf.write("\2\2\2\u01ca\u01d1\5E#\2\u01cb\u01d0\5[.\2\u01cc\u01d0")
        buf.write("\5_\60\2\u01cd\u01d0\t\4\2\2\u01ce\u01d0\5\67\34\2\u01cf")
        buf.write("\u01cb\3\2\2\2\u01cf\u01cc\3\2\2\2\u01cf\u01cd\3\2\2\2")
        buf.write("\u01cf\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3")
        buf.write("\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01d1")
        buf.write("\3\2\2\2\u01d4\u01d5\5E#\2\u01d5X\3\2\2\2\u01d6\u01da")
        buf.write("\5[.\2\u01d7\u01da\5_\60\2\u01d8\u01da\7a\2\2\u01d9\u01d6")
        buf.write("\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01d8\3\2\2\2\u01da")
        buf.write("Z\3\2\2\2\u01db\u01dd\t\5\2\2\u01dc\u01db\3\2\2\2\u01dd")
        buf.write("\\\3\2\2\2\u01de\u01df\t\6\2\2\u01df^\3\2\2\2\u01e0\u01e1")
        buf.write("\t\7\2\2\u01e1`\3\2\2\2\u01e2\u01e4\t\b\2\2\u01e3\u01e2")
        buf.write("\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5")
        buf.write("\u01e6\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\b\61\2")
        buf.write("\2\u01e8b\3\2\2\2\u01e9\u01eb\t\t\2\2\u01ea\u01e9\3\2")
        buf.write("\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01edd\3\2\2\2K\2fmpx{\u0082\u0085\u008c\u008f")
        buf.write("\u0095\u0098\u009e\u00a1\u00ad\u00b0\u00ba\u00bd\u00c7")
        buf.write("\u00ca\u00d3\u00d6\u00e3\u00e6\u00ef\u00f2\u00fb\u00fe")
        buf.write("\u0106\u0109\u0113\u0116\u011d\u0120\u0129\u012d\u013b")
        buf.write("\u013f\u0142\u0146\u0149\u014d\u0150\u0157\u015a\u0160")
        buf.write("\u0163\u0167\u016a\u016e\u0171\u0175\u0179\u017d\u0180")
        buf.write("\u0184\u0188\u018b\u018f\u01a1\u01a6\u01ad\u01b1\u01b8")
        buf.write("\u01ba\u01c3\u01c5\u01cf\u01d1\u01d9\u01dc\u01e5\u01ec")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class GraphQueryLanguageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    FUN = 1
    LOAD = 2
    SET = 3
    ADD = 4
    OF = 5
    TO = 6
    VERTICES = 7
    LABELS = 8
    SELECT = 9
    EDGES = 10
    REACHABLE = 11
    START = 12
    FINAL = 13
    FROM = 14
    FILTER = 15
    MAP = 16
    PRINT = 17
    BOOL = 18
    TRUE = 19
    FALSE = 20
    ASSIGN = 21
    AND = 22
    OR = 23
    NOT = 24
    IN = 25
    KLEENE = 26
    DOT = 27
    COMMA = 28
    SEMICOLON = 29
    LCB = 30
    RCB = 31
    LP = 32
    RP = 33
    QUOT = 34
    TRIPLE_QUOT = 35
    COLON = 36
    DOUBLE_ARROW = 37
    ARROW = 38
    VAR = 39
    INT = 40
    CFG = 41
    STRING = 42
    PATH = 43
    ID_CHAR = 44
    CHAR = 45
    NONZERO_DIGIT = 46
    DIGIT = 47
    WS = 48
    EOL = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'TRUE'", "'FALSE'", "'\"'", "'\"\"\"'", "':'", "'=>'", "'->'" ]

    symbolicNames = [ "<INVALID>",
            "FUN", "LOAD", "SET", "ADD", "OF", "TO", "VERTICES", "LABELS", 
            "SELECT", "EDGES", "REACHABLE", "START", "FINAL", "FROM", "FILTER", 
            "MAP", "PRINT", "BOOL", "TRUE", "FALSE", "ASSIGN", "AND", "OR", 
            "NOT", "IN", "KLEENE", "DOT", "COMMA", "SEMICOLON", "LCB", "RCB", 
            "LP", "RP", "QUOT", "TRIPLE_QUOT", "COLON", "DOUBLE_ARROW", 
            "ARROW", "VAR", "INT", "CFG", "STRING", "PATH", "ID_CHAR", "CHAR", 
            "NONZERO_DIGIT", "DIGIT", "WS", "EOL" ]

    ruleNames = [ "FUN", "LOAD", "SET", "ADD", "OF", "TO", "VERTICES", "LABELS", 
                  "SELECT", "EDGES", "REACHABLE", "START", "FINAL", "FROM", 
                  "FILTER", "MAP", "PRINT", "BOOL", "TRUE", "FALSE", "ASSIGN", 
                  "AND", "OR", "NOT", "IN", "KLEENE", "DOT", "COMMA", "SEMICOLON", 
                  "LCB", "RCB", "LP", "RP", "QUOT", "TRIPLE_QUOT", "COLON", 
                  "DOUBLE_ARROW", "ARROW", "VAR", "INT", "CFG", "STRING", 
                  "PATH", "ID_CHAR", "CHAR", "NONZERO_DIGIT", "DIGIT", "WS", 
                  "EOL" ]

    grammarFileName = "GraphQueryLanguage.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


