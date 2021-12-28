# Generated from ./project/gql/grammar/GraphQueryLanguage.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u01a5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write('\4\37\t\37\4 \t \4!\t!\4"\t"\4#\t#\4$\t$\4%\t%\3\2\5')
        buf.write("\2L\n\2\3\2\5\2O\n\2\3\2\3\2\3\2\5\2T\n\2\6\2V\n\2\r\2")
        buf.write("\16\2W\3\2\3\2\3\3\3\3\3\3\3\3\5\3`\n\3\3\3\3\3\5\3d\n")
        buf.write("\3\3\3\3\3\5\3h\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4v\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u0086\n\4\f\4\16\4\u0089")
        buf.write("\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u0096\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\u00a0\n")
        buf.write("\7\3\7\3\7\3\7\5\7\u00a5\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u00ac")
        buf.write("\n\b\3\b\3\b\3\b\5\b\u00b1\n\b\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00b8\n\t\3\t\3\t\3\t\5\t\u00bd\n\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u00c4\n\n\3\n\3\n\3\n\5\n\u00c9\n\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00d6")
        buf.write("\n\13\3\f\3\f\3\r\3\r\3\r\5\r\u00dd\n\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00ed\n\16\3\17\3\17\3\17\5\17\u00f2\n\17\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00ff\n\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\5\24\u010e\n\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u0115\n\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u011d\n\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u0125\n\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u012d\n")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\5\31\u0134\n\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\36\7\36\u0145\n\36\f\36\16\36\u0148\13\36\3\36")
        buf.write("\5\36\u014b\n\36\3\36\3\36\5\36\u014f\n\36\3\37\3\37\3")
        buf.write("\37\7\37\u0154\n\37\f\37\16\37\u0157\13\37\3\37\5\37\u015a")
        buf.write("\n\37\3\37\3\37\3 \3 \3 \3 \7 \u0162\n \f \16 \u0165\13")
        buf.write(' \3 \5 \u0168\n \3 \3 \3!\3!\3"\3"\3"\3"\3"\3"\3')
        buf.write('"\3"\3"\3"\3"\3"\3"\3"\3"\3"\3"\3"\3"\3"')
        buf.write('\3"\3"\3"\3"\3"\3"\3"\3"\3"\3"\5"\u018c\n"')
        buf.write("\3#\3#\3#\7#\u0191\n#\f#\16#\u0194\13#\3#\5#\u0197\n#")
        buf.write("\3#\5#\u019a\n#\3$\3$\3$\3$\3$\5$\u01a1\n$\3%\3%\3%\2")
        buf.write('\3\6&\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 "$&(*,.')
        buf.write("\60\62\64\668:<>@BDFH\2\2\2\u01c4\2U\3\2\2\2\4g\3\2\2")
        buf.write("\2\6u\3\2\2\2\b\u0095\3\2\2\2\n\u0097\3\2\2\2\f\u009a")
        buf.write("\3\2\2\2\16\u00a6\3\2\2\2\20\u00b2\3\2\2\2\22\u00be\3")
        buf.write("\2\2\2\24\u00d5\3\2\2\2\26\u00d7\3\2\2\2\30\u00dc\3\2")
        buf.write("\2\2\32\u00ec\3\2\2\2\34\u00f1\3\2\2\2\36\u00f3\3\2\2")
        buf.write('\2 \u00fe\3\2\2\2"\u0100\3\2\2\2$\u0104\3\2\2\2&\u0108')
        buf.write("\3\2\2\2(\u010f\3\2\2\2*\u0116\3\2\2\2,\u011e\3\2\2\2")
        buf.write(".\u0126\3\2\2\2\60\u012e\3\2\2\2\62\u0135\3\2\2\2\64\u013b")
        buf.write("\3\2\2\2\66\u013d\3\2\2\28\u013f\3\2\2\2:\u014e\3\2\2")
        buf.write("\2<\u0150\3\2\2\2>\u015d\3\2\2\2@\u016b\3\2\2\2B\u018b")
        buf.write("\3\2\2\2D\u0199\3\2\2\2F\u01a0\3\2\2\2H\u01a2\3\2\2\2")
        buf.write("JL\7\63\2\2KJ\3\2\2\2KL\3\2\2\2LN\3\2\2\2MO\7\62\2\2N")
        buf.write("M\3\2\2\2NO\3\2\2\2OP\3\2\2\2PQ\5\4\3\2QS\7\37\2\2RT\7")
        buf.write("\63\2\2SR\3\2\2\2ST\3\2\2\2TV\3\2\2\2UK\3\2\2\2VW\3\2")
        buf.write("\2\2WU\3\2\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\2\2\3Z\3\3\2\2")
        buf.write("\2[\\\7\23\2\2\\h\5\6\4\2]_\5@!\2^`\7\62\2\2_^\3\2\2\2")
        buf.write("_`\3\2\2\2`a\3\2\2\2ac\7\27\2\2bd\7\62\2\2cb\3\2\2\2c")
        buf.write("d\3\2\2\2de\3\2\2\2ef\5\6\4\2fh\3\2\2\2g[\3\2\2\2g]\3")
        buf.write('\2\2\2h\5\3\2\2\2ij\b\4\1\2jk\7"\2\2kl\5\6\4\2lm\7#\2')
        buf.write('\2mv\3\2\2\2nv\5 \21\2ov\5"\22\2pv\5$\23\2qv\5@!\2rv')
        buf.write("\5F$\2st\7\32\2\2tv\5\6\4\bui\3\2\2\2un\3\2\2\2uo\3\2")
        buf.write("\2\2up\3\2\2\2uq\3\2\2\2ur\3\2\2\2us\3\2\2\2v\u0087\3")
        buf.write("\2\2\2wx\f\7\2\2xy\7\33\2\2y\u0086\5\6\4\bz{\f\6\2\2{")
        buf.write("|\7\30\2\2|\u0086\5\6\4\7}~\f\5\2\2~\177\7\35\2\2\177")
        buf.write("\u0086\5\6\4\6\u0080\u0081\f\4\2\2\u0081\u0082\7\31\2")
        buf.write("\2\u0082\u0086\5\6\4\5\u0083\u0084\f\3\2\2\u0084\u0086")
        buf.write("\7\34\2\2\u0085w\3\2\2\2\u0085z\3\2\2\2\u0085}\3\2\2\2")
        buf.write("\u0085\u0080\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0089\3")
        buf.write("\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\7")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u0096\5\n\6\2\u008b")
        buf.write("\u0096\5\64\33\2\u008c\u0096\5\66\34\2\u008d\u0096\5\f")
        buf.write("\7\2\u008e\u0096\5\16\b\2\u008f\u0096\5\20\t\2\u0090\u0096")
        buf.write('\5\22\n\2\u0091\u0092\7"\2\2\u0092\u0093\5\b\5\2\u0093')
        buf.write("\u0094\7#\2\2\u0094\u0096\3\2\2\2\u0095\u008a\3\2\2\2")
        buf.write("\u0095\u008b\3\2\2\2\u0095\u008c\3\2\2\2\u0095\u008d\3")
        buf.write("\2\2\2\u0095\u008e\3\2\2\2\u0095\u008f\3\2\2\2\u0095\u0090")
        buf.write("\3\2\2\2\u0095\u0091\3\2\2\2\u0096\t\3\2\2\2\u0097\u0098")
        buf.write("\7\4\2\2\u0098\u0099\58\35\2\u0099\13\3\2\2\2\u009a\u009b")
        buf.write("\7\5\2\2\u009b\u009c\7\16\2\2\u009c\u009f\7\7\2\2\u009d")
        buf.write("\u00a0\5\b\5\2\u009e\u00a0\5@!\2\u009f\u009d\3\2\2\2\u009f")
        buf.write("\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a4\7\b\2\2")
        buf.write("\u00a2\u00a5\5\24\13\2\u00a3\u00a5\5@!\2\u00a4\u00a2\3")
        buf.write("\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\r\3\2\2\2\u00a6\u00a7")
        buf.write("\7\5\2\2\u00a7\u00a8\7\17\2\2\u00a8\u00ab\7\7\2\2\u00a9")
        buf.write("\u00ac\5\b\5\2\u00aa\u00ac\5@!\2\u00ab\u00a9\3\2\2\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00b0\7\b\2\2")
        buf.write("\u00ae\u00b1\5\24\13\2\u00af\u00b1\5@!\2\u00b0\u00ae\3")
        buf.write("\2\2\2\u00b0\u00af\3\2\2\2\u00b1\17\3\2\2\2\u00b2\u00b3")
        buf.write("\7\6\2\2\u00b3\u00b4\7\16\2\2\u00b4\u00b7\7\7\2\2\u00b5")
        buf.write("\u00b8\5\b\5\2\u00b6\u00b8\5@!\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bc\7\b\2\2")
        buf.write("\u00ba\u00bd\5\24\13\2\u00bb\u00bd\5@!\2\u00bc\u00ba\3")
        buf.write("\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\21\3\2\2\2\u00be\u00bf")
        buf.write("\7\6\2\2\u00bf\u00c0\7\17\2\2\u00c0\u00c3\7\7\2\2\u00c1")
        buf.write("\u00c4\5\b\5\2\u00c2\u00c4\5@!\2\u00c3\u00c1\3\2\2\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c8\7\b\2\2")
        buf.write("\u00c6\u00c9\5\24\13\2\u00c7\u00c9\5@!\2\u00c8\u00c6\3")
        buf.write("\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\23\3\2\2\2\u00ca\u00d6")
        buf.write("\5\26\f\2\u00cb\u00d6\5\62\32\2\u00cc\u00d6\5:\36\2\u00cd")
        buf.write("\u00d6\5*\26\2\u00ce\u00d6\5,\27\2\u00cf\u00d6\5.\30\2")
        buf.write('\u00d0\u00d6\5\60\31\2\u00d1\u00d2\7"\2\2\u00d2\u00d3')
        buf.write("\5\24\13\2\u00d3\u00d4\7#\2\2\u00d4\u00d6\3\2\2\2\u00d5")
        buf.write("\u00ca\3\2\2\2\u00d5\u00cb\3\2\2\2\u00d5\u00cc\3\2\2\2")
        buf.write("\u00d5\u00cd\3\2\2\2\u00d5\u00ce\3\2\2\2\u00d5\u00cf\3")
        buf.write("\2\2\2\u00d5\u00d0\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d6\25")
        buf.write("\3\2\2\2\u00d7\u00d8\7*\2\2\u00d8\27\3\2\2\2\u00d9\u00dd")
        buf.write("\5\32\16\2\u00da\u00dd\5> \2\u00db\u00dd\5&\24\2\u00dc")
        buf.write("\u00d9\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3\2\2\2")
        buf.write('\u00dd\31\3\2\2\2\u00de\u00df\7"\2\2\u00df\u00e0\5\26')
        buf.write("\f\2\u00e0\u00e1\7\36\2\2\u00e1\u00e2\5\36\20\2\u00e2")
        buf.write("\u00e3\7\36\2\2\u00e3\u00e4\5\26\f\2\u00e4\u00e5\7#\2")
        buf.write('\2\u00e5\u00ed\3\2\2\2\u00e6\u00e7\7"\2\2\u00e7\u00e8')
        buf.write("\5\26\f\2\u00e8\u00e9\7\36\2\2\u00e9\u00ea\5\26\f\2\u00ea")
        buf.write("\u00eb\7#\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00de\3\2\2\2")
        buf.write("\u00ec\u00e6\3\2\2\2\u00ed\33\3\2\2\2\u00ee\u00f2\5\36")
        buf.write("\20\2\u00ef\u00f2\5<\37\2\u00f0\u00f2\5(\25\2\u00f1\u00ee")
        buf.write("\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2")
        buf.write("\35\3\2\2\2\u00f3\u00f4\5\66\34\2\u00f4\37\3\2\2\2\u00f5")
        buf.write("\u00f6\7\3\2\2\u00f6\u00f7\5D#\2\u00f7\u00f8\7'\2\2\u00f8")
        buf.write('\u00f9\5\6\4\2\u00f9\u00ff\3\2\2\2\u00fa\u00fb\7"\2\2')
        buf.write("\u00fb\u00fc\5 \21\2\u00fc\u00fd\7#\2\2\u00fd\u00ff\3")
        buf.write("\2\2\2\u00fe\u00f5\3\2\2\2\u00fe\u00fa\3\2\2\2\u00ff!")
        buf.write("\3\2\2\2\u0100\u0101\7\22\2\2\u0101\u0102\5 \21\2\u0102")
        buf.write("\u0103\5\6\4\2\u0103#\3\2\2\2\u0104\u0105\7\21\2\2\u0105")
        buf.write("\u0106\5 \21\2\u0106\u0107\5\6\4\2\u0107%\3\2\2\2\u0108")
        buf.write("\u0109\7\13\2\2\u0109\u010a\7\f\2\2\u010a\u010d\7\20\2")
        buf.write("\2\u010b\u010e\5\b\5\2\u010c\u010e\5@!\2\u010d\u010b\3")
        buf.write("\2\2\2\u010d\u010c\3\2\2\2\u010e'\3\2\2\2\u010f\u0110")
        buf.write("\7\13\2\2\u0110\u0111\7\n\2\2\u0111\u0114\7\20\2\2\u0112")
        buf.write("\u0115\5\b\5\2\u0113\u0115\5@!\2\u0114\u0112\3\2\2\2\u0114")
        buf.write("\u0113\3\2\2\2\u0115)\3\2\2\2\u0116\u0117\7\13\2\2\u0117")
        buf.write("\u0118\7\r\2\2\u0118\u0119\7\t\2\2\u0119\u011c\7\20\2")
        buf.write("\2\u011a\u011d\5\b\5\2\u011b\u011d\5@!\2\u011c\u011a\3")
        buf.write("\2\2\2\u011c\u011b\3\2\2\2\u011d+\3\2\2\2\u011e\u011f")
        buf.write("\7\13\2\2\u011f\u0120\7\17\2\2\u0120\u0121\7\t\2\2\u0121")
        buf.write("\u0124\7\20\2\2\u0122\u0125\5\b\5\2\u0123\u0125\5@!\2")
        buf.write("\u0124\u0122\3\2\2\2\u0124\u0123\3\2\2\2\u0125-\3\2\2")
        buf.write("\2\u0126\u0127\7\13\2\2\u0127\u0128\7\16\2\2\u0128\u0129")
        buf.write("\7\t\2\2\u0129\u012c\7\20\2\2\u012a\u012d\5\b\5\2\u012b")
        buf.write("\u012d\5@!\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d")
        buf.write("/\3\2\2\2\u012e\u012f\7\13\2\2\u012f\u0130\7\t\2\2\u0130")
        buf.write("\u0133\7\20\2\2\u0131\u0134\5\b\5\2\u0132\u0134\5@!\2")
        buf.write("\u0133\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134\61\3\2")
        buf.write("\2\2\u0135\u0136\7 \2\2\u0136\u0137\7*\2\2\u0137\u0138")
        buf.write("\7&\2\2\u0138\u0139\7*\2\2\u0139\u013a\7!\2\2\u013a\63")
        buf.write("\3\2\2\2\u013b\u013c\7+\2\2\u013c\65\3\2\2\2\u013d\u013e")
        buf.write("\7,\2\2\u013e\67\3\2\2\2\u013f\u0140\7-\2\2\u01409\3\2")
        buf.write("\2\2\u0141\u0146\7 \2\2\u0142\u0143\7*\2\2\u0143\u0145")
        buf.write("\7\36\2\2\u0144\u0142\3\2\2\2\u0145\u0148\3\2\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u014a\3\2\2\2")
        buf.write("\u0148\u0146\3\2\2\2\u0149\u014b\7*\2\2\u014a\u0149\3")
        buf.write("\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014f")
        buf.write("\7!\2\2\u014d\u014f\5\62\32\2\u014e\u0141\3\2\2\2\u014e")
        buf.write("\u014d\3\2\2\2\u014f;\3\2\2\2\u0150\u0155\7 \2\2\u0151")
        buf.write("\u0152\7,\2\2\u0152\u0154\7\36\2\2\u0153\u0151\3\2\2\2")
        buf.write("\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3")
        buf.write("\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0158\u015a")
        buf.write("\7,\2\2\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015b\u015c\7!\2\2\u015c=\3\2\2\2\u015d")
        buf.write("\u0163\7 \2\2\u015e\u015f\5\32\16\2\u015f\u0160\7\36\2")
        buf.write("\2\u0160\u0162\3\2\2\2\u0161\u015e\3\2\2\2\u0162\u0165")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0168\5\32\16")
        buf.write("\2\u0167\u0166\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u016a\7!\2\2\u016a?\3\2\2\2\u016b\u016c")
        buf.write('\7)\2\2\u016cA\3\2\2\2\u016d\u016e\7"\2\2\u016e\u016f')
        buf.write("\5@!\2\u016f\u0170\7\36\2\2\u0170\u0171\5@!\2\u0171\u0172")
        buf.write('\7#\2\2\u0172\u018c\3\2\2\2\u0173\u0174\7"\2\2\u0174')
        buf.write("\u0175\5@!\2\u0175\u0176\7\36\2\2\u0176\u0177\5@!\2\u0177")
        buf.write("\u0178\7\36\2\2\u0178\u0179\5@!\2\u0179\u017a\7#\2\2\u017a")
        buf.write('\u018c\3\2\2\2\u017b\u017c\7"\2\2\u017c\u017d\7"\2\2')
        buf.write("\u017d\u017e\5@!\2\u017e\u017f\7\36\2\2\u017f\u0180\5")
        buf.write("@!\2\u0180\u0181\7#\2\2\u0181\u0182\7\36\2\2\u0182\u0183")
        buf.write('\5@!\2\u0183\u0184\7\36\2\2\u0184\u0185\7"\2\2\u0185')
        buf.write("\u0186\5@!\2\u0186\u0187\7\36\2\2\u0187\u0188\5@!\2\u0188")
        buf.write("\u0189\7#\2\2\u0189\u018a\7#\2\2\u018a\u018c\3\2\2\2\u018b")
        buf.write("\u016d\3\2\2\2\u018b\u0173\3\2\2\2\u018b\u017b\3\2\2\2")
        buf.write("\u018cC\3\2\2\2\u018d\u018e\5@!\2\u018e\u018f\7\36\2\2")
        buf.write("\u018f\u0191\3\2\2\2\u0190\u018d\3\2\2\2\u0191\u0194\3")
        buf.write("\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0196")
        buf.write("\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0197\5@!\2\u0196\u0195")
        buf.write("\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u019a\3\2\2\2\u0198")
        buf.write('\u019a\5B"\2\u0199\u0192\3\2\2\2\u0199\u0198\3\2\2\2')
        buf.write("\u019aE\3\2\2\2\u019b\u01a1\5H%\2\u019c\u01a1\5\b\5\2")
        buf.write("\u019d\u01a1\5\30\r\2\u019e\u01a1\5\34\17\2\u019f\u01a1")
        buf.write("\5\24\13\2\u01a0\u019b\3\2\2\2\u01a0\u019c\3\2\2\2\u01a0")
        buf.write("\u019d\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u019f\3\2\2\2")
        buf.write("\u01a1G\3\2\2\2\u01a2\u01a3\7\24\2\2\u01a3I\3\2\2\2,K")
        buf.write("NSW_cgu\u0085\u0087\u0095\u009f\u00a4\u00ab\u00b0\u00b7")
        buf.write("\u00bc\u00c3\u00c8\u00d5\u00dc\u00ec\u00f1\u00fe\u010d")
        buf.write("\u0114\u011c\u0124\u012c\u0133\u0146\u014a\u014e\u0155")
        buf.write("\u0159\u0163\u0167\u018b\u0192\u0196\u0199\u01a0")
        return buf.getvalue()


class GraphQueryLanguageParser(Parser):

    grammarFileName = "GraphQueryLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'TRUE'",
        "'FALSE'",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'\"'",
        '\'"""\'',
        "':'",
        "'=>'",
        "'->'",
    ]

    symbolicNames = [
        "<INVALID>",
        "FUN",
        "LOAD",
        "SET",
        "ADD",
        "OF",
        "TO",
        "VERTICES",
        "LABELS",
        "SELECT",
        "EDGES",
        "REACHABLE",
        "START",
        "FINAL",
        "FROM",
        "FILTER",
        "MAP",
        "PRINT",
        "BOOL",
        "TRUE",
        "FALSE",
        "ASSIGN",
        "AND",
        "OR",
        "NOT",
        "IN",
        "KLEENE",
        "DOT",
        "COMMA",
        "SEMICOLON",
        "LCB",
        "RCB",
        "LP",
        "RP",
        "QUOT",
        "TRIPLE_QUOT",
        "COLON",
        "DOUBLE_ARROW",
        "ARROW",
        "VAR",
        "INT",
        "CFG",
        "STRING",
        "PATH",
        "ID_CHAR",
        "CHAR",
        "NONZERO_DIGIT",
        "DIGIT",
        "WS",
        "EOL",
    ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_graph = 3
    RULE_load_graph = 4
    RULE_set_start = 5
    RULE_set_final = 6
    RULE_add_start = 7
    RULE_add_final = 8
    RULE_vertices = 9
    RULE_vertex = 10
    RULE_edges = 11
    RULE_edge = 12
    RULE_labels = 13
    RULE_label = 14
    RULE_anfunc = 15
    RULE_mapping = 16
    RULE_filtering = 17
    RULE_select_edges = 18
    RULE_select_labels = 19
    RULE_select_reachable = 20
    RULE_select_final = 21
    RULE_select_start = 22
    RULE_select_vertices = 23
    RULE_vertices_range = 24
    RULE_cfg = 25
    RULE_string = 26
    RULE_path = 27
    RULE_vertices_set = 28
    RULE_labels_set = 29
    RULE_edges_set = 30
    RULE_var = 31
    RULE_var_edge = 32
    RULE_variables = 33
    RULE_val = 34
    RULE_boolean = 35

    ruleNames = [
        "prog",
        "stmt",
        "expr",
        "graph",
        "load_graph",
        "set_start",
        "set_final",
        "add_start",
        "add_final",
        "vertices",
        "vertex",
        "edges",
        "edge",
        "labels",
        "label",
        "anfunc",
        "mapping",
        "filtering",
        "select_edges",
        "select_labels",
        "select_reachable",
        "select_final",
        "select_start",
        "select_vertices",
        "vertices_range",
        "cfg",
        "string",
        "path",
        "vertices_set",
        "labels_set",
        "edges_set",
        "var",
        "var_edge",
        "variables",
        "val",
        "boolean",
    ]

    EOF = Token.EOF
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

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class ProgContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GraphQueryLanguageParser.EOF, 0)

        def stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryLanguageParser.StmtContext)
            else:
                return self.getTypedRuleContext(GraphQueryLanguageParser.StmtContext, i)

        def SEMICOLON(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.SEMICOLON)
            else:
                return self.getToken(GraphQueryLanguageParser.SEMICOLON, i)

        def EOL(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.EOL)
            else:
                return self.getToken(GraphQueryLanguageParser.EOL, i)

        def WS(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.WS)
            else:
                return self.getToken(GraphQueryLanguageParser.WS, i)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_prog

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProg"):
                listener.enterProg(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProg"):
                listener.exitProg(self)

    def prog(self):

        localctx = GraphQueryLanguageParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GraphQueryLanguageParser.EOL:
                    self.state = 72
                    self.match(GraphQueryLanguageParser.EOL)

                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GraphQueryLanguageParser.WS:
                    self.state = 75
                    self.match(GraphQueryLanguageParser.WS)

                self.state = 78
                self.stmt()
                self.state = 79
                self.match(GraphQueryLanguageParser.SEMICOLON)
                self.state = 81
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
                if la_ == 1:
                    self.state = 80
                    self.match(GraphQueryLanguageParser.EOL)

                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << GraphQueryLanguageParser.PRINT)
                                | (1 << GraphQueryLanguageParser.VAR)
                                | (1 << GraphQueryLanguageParser.WS)
                                | (1 << GraphQueryLanguageParser.EOL)
                            )
                        )
                        != 0
                    )
                ):
                    break

            self.state = 87
            self.match(GraphQueryLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(GraphQueryLanguageParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.ExprContext, 0)

        def var(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, 0)

        def ASSIGN(self):
            return self.getToken(GraphQueryLanguageParser.ASSIGN, 0)

        def WS(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.WS)
            else:
                return self.getToken(GraphQueryLanguageParser.WS, i)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmt"):
                listener.enterStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmt"):
                listener.exitStmt(self)

    def stmt(self):

        localctx = GraphQueryLanguageParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0  # Token type
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GraphQueryLanguageParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(GraphQueryLanguageParser.PRINT)
                self.state = 90
                self.expr(0)
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.var()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GraphQueryLanguageParser.WS:
                    self.state = 92
                    self.match(GraphQueryLanguageParser.WS)

                self.state = 95
                self.match(GraphQueryLanguageParser.ASSIGN)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GraphQueryLanguageParser.WS:
                    self.state = 96
                    self.match(GraphQueryLanguageParser.WS)

                self.state = 99
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(GraphQueryLanguageParser.LP, 0)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(GraphQueryLanguageParser.ExprContext, i)

        def RP(self):
            return self.getToken(GraphQueryLanguageParser.RP, 0)

        def anfunc(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.AnfuncContext, 0)

        def mapping(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.MappingContext, 0)

        def filtering(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.FilteringContext, 0
            )

        def var(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, 0)

        def val(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.ValContext, 0)

        def NOT(self):
            return self.getToken(GraphQueryLanguageParser.NOT, 0)

        def IN(self):
            return self.getToken(GraphQueryLanguageParser.IN, 0)

        def AND(self):
            return self.getToken(GraphQueryLanguageParser.AND, 0)

        def DOT(self):
            return self.getToken(GraphQueryLanguageParser.DOT, 0)

        def OR(self):
            return self.getToken(GraphQueryLanguageParser.OR, 0)

        def KLEENE(self):
            return self.getToken(GraphQueryLanguageParser.KLEENE, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_expr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpr"):
                listener.enterExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpr"):
                listener.exitExpr(self)

    def expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GraphQueryLanguageParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 7, self._ctx)
            if la_ == 1:
                self.state = 104
                self.match(GraphQueryLanguageParser.LP)
                self.state = 105
                self.expr(0)
                self.state = 106
                self.match(GraphQueryLanguageParser.RP)
                pass

            elif la_ == 2:
                self.state = 108
                self.anfunc()
                pass

            elif la_ == 3:
                self.state = 109
                self.mapping()
                pass

            elif la_ == 4:
                self.state = 110
                self.filtering()
                pass

            elif la_ == 5:
                self.state = 111
                self.var()
                pass

            elif la_ == 6:
                self.state = 112
                self.val()
                pass

            elif la_ == 7:
                self.state = 113
                self.match(GraphQueryLanguageParser.NOT)
                self.state = 114
                self.expr(6)
                pass

            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 9, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 131
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 8, self._ctx)
                    if la_ == 1:
                        localctx = GraphQueryLanguageParser.ExprContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr
                        )
                        self.state = 117
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 5)"
                            )
                        self.state = 118
                        self.match(GraphQueryLanguageParser.IN)
                        self.state = 119
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = GraphQueryLanguageParser.ExprContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr
                        )
                        self.state = 120
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 4)"
                            )
                        self.state = 121
                        self.match(GraphQueryLanguageParser.AND)
                        self.state = 122
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = GraphQueryLanguageParser.ExprContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr
                        )
                        self.state = 123
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 3)"
                            )
                        self.state = 124
                        self.match(GraphQueryLanguageParser.DOT)
                        self.state = 125
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = GraphQueryLanguageParser.ExprContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr
                        )
                        self.state = 126
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 2)"
                            )
                        self.state = 127
                        self.match(GraphQueryLanguageParser.OR)
                        self.state = 128
                        self.expr(3)
                        pass

                    elif la_ == 5:
                        localctx = GraphQueryLanguageParser.ExprContext(
                            self, _parentctx, _parentState
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr
                        )
                        self.state = 129
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 1)"
                            )
                        self.state = 130
                        self.match(GraphQueryLanguageParser.KLEENE)
                        pass

                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 9, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class GraphContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def load_graph(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Load_graphContext, 0
            )

        def cfg(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.CfgContext, 0)

        def string(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.StringContext, 0)

        def set_start(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Set_startContext, 0
            )

        def set_final(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Set_finalContext, 0
            )

        def add_start(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Add_startContext, 0
            )

        def add_final(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Add_finalContext, 0
            )

        def LP(self):
            return self.getToken(GraphQueryLanguageParser.LP, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def RP(self):
            return self.getToken(GraphQueryLanguageParser.RP, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_graph

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterGraph"):
                listener.enterGraph(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitGraph"):
                listener.exitGraph(self)

    def graph(self):

        localctx = GraphQueryLanguageParser.GraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_graph)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 10, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.load_graph()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.cfg()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.string()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.set_start()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.set_final()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                self.add_start()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 142
                self.add_final()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 143
                self.match(GraphQueryLanguageParser.LP)
                self.state = 144
                self.graph()
                self.state = 145
                self.match(GraphQueryLanguageParser.RP)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Load_graphContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(GraphQueryLanguageParser.LOAD, 0)

        def path(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.PathContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_load_graph

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLoad_graph"):
                listener.enterLoad_graph(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLoad_graph"):
                listener.exitLoad_graph(self)

    def load_graph(self):

        localctx = GraphQueryLanguageParser.Load_graphContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 8, self.RULE_load_graph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(GraphQueryLanguageParser.LOAD)
            self.state = 150
            self.path()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_startContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(GraphQueryLanguageParser.SET, 0)

        def START(self):
            return self.getToken(GraphQueryLanguageParser.START, 0)

        def OF(self):
            return self.getToken(GraphQueryLanguageParser.OF, 0)

        def TO(self):
            return self.getToken(GraphQueryLanguageParser.TO, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def var(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryLanguageParser.VarContext)
            else:
                return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, i)

        def vertices(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VerticesContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_set_start

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSet_start"):
                listener.enterSet_start(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSet_start"):
                listener.exitSet_start(self)

    def set_start(self):

        localctx = GraphQueryLanguageParser.Set_startContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 10, self.RULE_set_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(GraphQueryLanguageParser.SET)
            self.state = 153
            self.match(GraphQueryLanguageParser.START)
            self.state = 154
            self.match(GraphQueryLanguageParser.OF)
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.LOAD,
                GraphQueryLanguageParser.SET,
                GraphQueryLanguageParser.ADD,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.CFG,
                GraphQueryLanguageParser.STRING,
            ]:
                self.state = 155
                self.graph()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 156
                self.var()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 159
            self.match(GraphQueryLanguageParser.TO)
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.SELECT,
                GraphQueryLanguageParser.LCB,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.INT,
            ]:
                self.state = 160
                self.vertices()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 161
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Set_finalContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(GraphQueryLanguageParser.SET, 0)

        def FINAL(self):
            return self.getToken(GraphQueryLanguageParser.FINAL, 0)

        def OF(self):
            return self.getToken(GraphQueryLanguageParser.OF, 0)

        def TO(self):
            return self.getToken(GraphQueryLanguageParser.TO, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def var(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryLanguageParser.VarContext)
            else:
                return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, i)

        def vertices(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VerticesContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_set_final

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSet_final"):
                listener.enterSet_final(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSet_final"):
                listener.exitSet_final(self)

    def set_final(self):

        localctx = GraphQueryLanguageParser.Set_finalContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 12, self.RULE_set_final)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(GraphQueryLanguageParser.SET)
            self.state = 165
            self.match(GraphQueryLanguageParser.FINAL)
            self.state = 166
            self.match(GraphQueryLanguageParser.OF)
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.LOAD,
                GraphQueryLanguageParser.SET,
                GraphQueryLanguageParser.ADD,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.CFG,
                GraphQueryLanguageParser.STRING,
            ]:
                self.state = 167
                self.graph()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 168
                self.var()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 171
            self.match(GraphQueryLanguageParser.TO)
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.SELECT,
                GraphQueryLanguageParser.LCB,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.INT,
            ]:
                self.state = 172
                self.vertices()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 173
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Add_startContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(GraphQueryLanguageParser.ADD, 0)

        def START(self):
            return self.getToken(GraphQueryLanguageParser.START, 0)

        def OF(self):
            return self.getToken(GraphQueryLanguageParser.OF, 0)

        def TO(self):
            return self.getToken(GraphQueryLanguageParser.TO, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def var(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryLanguageParser.VarContext)
            else:
                return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, i)

        def vertices(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VerticesContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_add_start

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAdd_start"):
                listener.enterAdd_start(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAdd_start"):
                listener.exitAdd_start(self)

    def add_start(self):

        localctx = GraphQueryLanguageParser.Add_startContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 14, self.RULE_add_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(GraphQueryLanguageParser.ADD)
            self.state = 177
            self.match(GraphQueryLanguageParser.START)
            self.state = 178
            self.match(GraphQueryLanguageParser.OF)
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.LOAD,
                GraphQueryLanguageParser.SET,
                GraphQueryLanguageParser.ADD,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.CFG,
                GraphQueryLanguageParser.STRING,
            ]:
                self.state = 179
                self.graph()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 180
                self.var()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 183
            self.match(GraphQueryLanguageParser.TO)
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.SELECT,
                GraphQueryLanguageParser.LCB,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.INT,
            ]:
                self.state = 184
                self.vertices()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 185
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Add_finalContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(GraphQueryLanguageParser.ADD, 0)

        def FINAL(self):
            return self.getToken(GraphQueryLanguageParser.FINAL, 0)

        def OF(self):
            return self.getToken(GraphQueryLanguageParser.OF, 0)

        def TO(self):
            return self.getToken(GraphQueryLanguageParser.TO, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def var(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryLanguageParser.VarContext)
            else:
                return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, i)

        def vertices(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VerticesContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_add_final

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAdd_final"):
                listener.enterAdd_final(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAdd_final"):
                listener.exitAdd_final(self)

    def add_final(self):

        localctx = GraphQueryLanguageParser.Add_finalContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 16, self.RULE_add_final)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(GraphQueryLanguageParser.ADD)
            self.state = 189
            self.match(GraphQueryLanguageParser.FINAL)
            self.state = 190
            self.match(GraphQueryLanguageParser.OF)
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.LOAD,
                GraphQueryLanguageParser.SET,
                GraphQueryLanguageParser.ADD,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.CFG,
                GraphQueryLanguageParser.STRING,
            ]:
                self.state = 191
                self.graph()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 192
                self.var()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 195
            self.match(GraphQueryLanguageParser.TO)
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.SELECT,
                GraphQueryLanguageParser.LCB,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.INT,
            ]:
                self.state = 196
                self.vertices()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 197
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VerticesContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertex(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VertexContext, 0)

        def vertices_range(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Vertices_rangeContext, 0
            )

        def vertices_set(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Vertices_setContext, 0
            )

        def select_reachable(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Select_reachableContext, 0
            )

        def select_final(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Select_finalContext, 0
            )

        def select_start(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Select_startContext, 0
            )

        def select_vertices(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Select_verticesContext, 0
            )

        def LP(self):
            return self.getToken(GraphQueryLanguageParser.LP, 0)

        def vertices(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VerticesContext, 0)

        def RP(self):
            return self.getToken(GraphQueryLanguageParser.RP, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_vertices

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVertices"):
                listener.enterVertices(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVertices"):
                listener.exitVertices(self)

    def vertices(self):

        localctx = GraphQueryLanguageParser.VerticesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vertices)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 19, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.vertex()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.vertices_range()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.vertices_set()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.select_reachable()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.select_final()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 205
                self.select_start()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 206
                self.select_vertices()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 207
                self.match(GraphQueryLanguageParser.LP)
                self.state = 208
                self.vertices()
                self.state = 209
                self.match(GraphQueryLanguageParser.RP)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VertexContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GraphQueryLanguageParser.INT, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_vertex

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVertex"):
                listener.enterVertex(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVertex"):
                listener.exitVertex(self)

    def vertex(self):

        localctx = GraphQueryLanguageParser.VertexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_vertex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(GraphQueryLanguageParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EdgesContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edge(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.EdgeContext, 0)

        def edges_set(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Edges_setContext, 0
            )

        def select_edges(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Select_edgesContext, 0
            )

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_edges

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEdges"):
                listener.enterEdges(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEdges"):
                listener.exitEdges(self)

    def edges(self):

        localctx = GraphQueryLanguageParser.EdgesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_edges)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GraphQueryLanguageParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.edge()
                pass
            elif token in [GraphQueryLanguageParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.edges_set()
                pass
            elif token in [GraphQueryLanguageParser.SELECT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.select_edges()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EdgeContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(GraphQueryLanguageParser.LP, 0)

        def vertex(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryLanguageParser.VertexContext)
            else:
                return self.getTypedRuleContext(
                    GraphQueryLanguageParser.VertexContext, i
                )

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.COMMA)
            else:
                return self.getToken(GraphQueryLanguageParser.COMMA, i)

        def label(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.LabelContext, 0)

        def RP(self):
            return self.getToken(GraphQueryLanguageParser.RP, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_edge

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEdge"):
                listener.enterEdge(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEdge"):
                listener.exitEdge(self)

    def edge(self):

        localctx = GraphQueryLanguageParser.EdgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_edge)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 21, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(GraphQueryLanguageParser.LP)
                self.state = 221
                self.vertex()
                self.state = 222
                self.match(GraphQueryLanguageParser.COMMA)
                self.state = 223
                self.label()
                self.state = 224
                self.match(GraphQueryLanguageParser.COMMA)
                self.state = 225
                self.vertex()
                self.state = 226
                self.match(GraphQueryLanguageParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(GraphQueryLanguageParser.LP)
                self.state = 229
                self.vertex()
                self.state = 230
                self.match(GraphQueryLanguageParser.COMMA)
                self.state = 231
                self.vertex()
                self.state = 232
                self.match(GraphQueryLanguageParser.RP)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelsContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.LabelContext, 0)

        def labels_set(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Labels_setContext, 0
            )

        def select_labels(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Select_labelsContext, 0
            )

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_labels

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLabels"):
                listener.enterLabels(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLabels"):
                listener.exitLabels(self)

    def labels(self):

        localctx = GraphQueryLanguageParser.LabelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_labels)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GraphQueryLanguageParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.label()
                pass
            elif token in [GraphQueryLanguageParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.labels_set()
                pass
            elif token in [GraphQueryLanguageParser.SELECT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.select_labels()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.StringContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_label

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLabel"):
                listener.enterLabel(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLabel"):
                listener.exitLabel(self)

    def label(self):

        localctx = GraphQueryLanguageParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AnfuncContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUN(self):
            return self.getToken(GraphQueryLanguageParser.FUN, 0)

        def variables(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.VariablesContext, 0
            )

        def DOUBLE_ARROW(self):
            return self.getToken(GraphQueryLanguageParser.DOUBLE_ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.ExprContext, 0)

        def LP(self):
            return self.getToken(GraphQueryLanguageParser.LP, 0)

        def anfunc(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.AnfuncContext, 0)

        def RP(self):
            return self.getToken(GraphQueryLanguageParser.RP, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_anfunc

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAnfunc"):
                listener.enterAnfunc(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAnfunc"):
                listener.exitAnfunc(self)

    def anfunc(self):

        localctx = GraphQueryLanguageParser.AnfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_anfunc)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GraphQueryLanguageParser.FUN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(GraphQueryLanguageParser.FUN)
                self.state = 244
                self.variables()
                self.state = 245
                self.match(GraphQueryLanguageParser.DOUBLE_ARROW)
                self.state = 246
                self.expr(0)
                pass
            elif token in [GraphQueryLanguageParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(GraphQueryLanguageParser.LP)
                self.state = 249
                self.anfunc()
                self.state = 250
                self.match(GraphQueryLanguageParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MappingContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP(self):
            return self.getToken(GraphQueryLanguageParser.MAP, 0)

        def anfunc(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.AnfuncContext, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.ExprContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_mapping

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMapping"):
                listener.enterMapping(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMapping"):
                listener.exitMapping(self)

    def mapping(self):

        localctx = GraphQueryLanguageParser.MappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_mapping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(GraphQueryLanguageParser.MAP)
            self.state = 255
            self.anfunc()
            self.state = 256
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FilteringContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(GraphQueryLanguageParser.FILTER, 0)

        def anfunc(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.AnfuncContext, 0)

        def expr(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.ExprContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_filtering

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFiltering"):
                listener.enterFiltering(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFiltering"):
                listener.exitFiltering(self)

    def filtering(self):

        localctx = GraphQueryLanguageParser.FilteringContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 34, self.RULE_filtering)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(GraphQueryLanguageParser.FILTER)
            self.state = 259
            self.anfunc()
            self.state = 260
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_edgesContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(GraphQueryLanguageParser.SELECT, 0)

        def EDGES(self):
            return self.getToken(GraphQueryLanguageParser.EDGES, 0)

        def FROM(self):
            return self.getToken(GraphQueryLanguageParser.FROM, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def var(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_select_edges

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSelect_edges"):
                listener.enterSelect_edges(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSelect_edges"):
                listener.exitSelect_edges(self)

    def select_edges(self):

        localctx = GraphQueryLanguageParser.Select_edgesContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 36, self.RULE_select_edges)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(GraphQueryLanguageParser.SELECT)
            self.state = 263
            self.match(GraphQueryLanguageParser.EDGES)
            self.state = 264
            self.match(GraphQueryLanguageParser.FROM)
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.LOAD,
                GraphQueryLanguageParser.SET,
                GraphQueryLanguageParser.ADD,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.CFG,
                GraphQueryLanguageParser.STRING,
            ]:
                self.state = 265
                self.graph()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 266
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_labelsContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(GraphQueryLanguageParser.SELECT, 0)

        def LABELS(self):
            return self.getToken(GraphQueryLanguageParser.LABELS, 0)

        def FROM(self):
            return self.getToken(GraphQueryLanguageParser.FROM, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def var(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_select_labels

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSelect_labels"):
                listener.enterSelect_labels(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSelect_labels"):
                listener.exitSelect_labels(self)

    def select_labels(self):

        localctx = GraphQueryLanguageParser.Select_labelsContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 38, self.RULE_select_labels)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(GraphQueryLanguageParser.SELECT)
            self.state = 270
            self.match(GraphQueryLanguageParser.LABELS)
            self.state = 271
            self.match(GraphQueryLanguageParser.FROM)
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.LOAD,
                GraphQueryLanguageParser.SET,
                GraphQueryLanguageParser.ADD,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.CFG,
                GraphQueryLanguageParser.STRING,
            ]:
                self.state = 272
                self.graph()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 273
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_reachableContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(GraphQueryLanguageParser.SELECT, 0)

        def REACHABLE(self):
            return self.getToken(GraphQueryLanguageParser.REACHABLE, 0)

        def VERTICES(self):
            return self.getToken(GraphQueryLanguageParser.VERTICES, 0)

        def FROM(self):
            return self.getToken(GraphQueryLanguageParser.FROM, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def var(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_select_reachable

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSelect_reachable"):
                listener.enterSelect_reachable(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSelect_reachable"):
                listener.exitSelect_reachable(self)

    def select_reachable(self):

        localctx = GraphQueryLanguageParser.Select_reachableContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 40, self.RULE_select_reachable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(GraphQueryLanguageParser.SELECT)
            self.state = 277
            self.match(GraphQueryLanguageParser.REACHABLE)
            self.state = 278
            self.match(GraphQueryLanguageParser.VERTICES)
            self.state = 279
            self.match(GraphQueryLanguageParser.FROM)
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.LOAD,
                GraphQueryLanguageParser.SET,
                GraphQueryLanguageParser.ADD,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.CFG,
                GraphQueryLanguageParser.STRING,
            ]:
                self.state = 280
                self.graph()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 281
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_finalContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(GraphQueryLanguageParser.SELECT, 0)

        def FINAL(self):
            return self.getToken(GraphQueryLanguageParser.FINAL, 0)

        def VERTICES(self):
            return self.getToken(GraphQueryLanguageParser.VERTICES, 0)

        def FROM(self):
            return self.getToken(GraphQueryLanguageParser.FROM, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def var(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_select_final

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSelect_final"):
                listener.enterSelect_final(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSelect_final"):
                listener.exitSelect_final(self)

    def select_final(self):

        localctx = GraphQueryLanguageParser.Select_finalContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 42, self.RULE_select_final)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(GraphQueryLanguageParser.SELECT)
            self.state = 285
            self.match(GraphQueryLanguageParser.FINAL)
            self.state = 286
            self.match(GraphQueryLanguageParser.VERTICES)
            self.state = 287
            self.match(GraphQueryLanguageParser.FROM)
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.LOAD,
                GraphQueryLanguageParser.SET,
                GraphQueryLanguageParser.ADD,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.CFG,
                GraphQueryLanguageParser.STRING,
            ]:
                self.state = 288
                self.graph()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 289
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_startContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(GraphQueryLanguageParser.SELECT, 0)

        def START(self):
            return self.getToken(GraphQueryLanguageParser.START, 0)

        def VERTICES(self):
            return self.getToken(GraphQueryLanguageParser.VERTICES, 0)

        def FROM(self):
            return self.getToken(GraphQueryLanguageParser.FROM, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def var(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_select_start

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSelect_start"):
                listener.enterSelect_start(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSelect_start"):
                listener.exitSelect_start(self)

    def select_start(self):

        localctx = GraphQueryLanguageParser.Select_startContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 44, self.RULE_select_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(GraphQueryLanguageParser.SELECT)
            self.state = 293
            self.match(GraphQueryLanguageParser.START)
            self.state = 294
            self.match(GraphQueryLanguageParser.VERTICES)
            self.state = 295
            self.match(GraphQueryLanguageParser.FROM)
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.LOAD,
                GraphQueryLanguageParser.SET,
                GraphQueryLanguageParser.ADD,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.CFG,
                GraphQueryLanguageParser.STRING,
            ]:
                self.state = 296
                self.graph()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 297
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Select_verticesContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(GraphQueryLanguageParser.SELECT, 0)

        def VERTICES(self):
            return self.getToken(GraphQueryLanguageParser.VERTICES, 0)

        def FROM(self):
            return self.getToken(GraphQueryLanguageParser.FROM, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def var(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_select_vertices

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSelect_vertices"):
                listener.enterSelect_vertices(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSelect_vertices"):
                listener.exitSelect_vertices(self)

    def select_vertices(self):

        localctx = GraphQueryLanguageParser.Select_verticesContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 46, self.RULE_select_vertices)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(GraphQueryLanguageParser.SELECT)
            self.state = 301
            self.match(GraphQueryLanguageParser.VERTICES)
            self.state = 302
            self.match(GraphQueryLanguageParser.FROM)
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.LOAD,
                GraphQueryLanguageParser.SET,
                GraphQueryLanguageParser.ADD,
                GraphQueryLanguageParser.LP,
                GraphQueryLanguageParser.CFG,
                GraphQueryLanguageParser.STRING,
            ]:
                self.state = 303
                self.graph()
                pass
            elif token in [GraphQueryLanguageParser.VAR]:
                self.state = 304
                self.var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Vertices_rangeContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(GraphQueryLanguageParser.LCB, 0)

        def INT(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.INT)
            else:
                return self.getToken(GraphQueryLanguageParser.INT, i)

        def COLON(self):
            return self.getToken(GraphQueryLanguageParser.COLON, 0)

        def RCB(self):
            return self.getToken(GraphQueryLanguageParser.RCB, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_vertices_range

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVertices_range"):
                listener.enterVertices_range(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVertices_range"):
                listener.exitVertices_range(self)

    def vertices_range(self):

        localctx = GraphQueryLanguageParser.Vertices_rangeContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 48, self.RULE_vertices_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(GraphQueryLanguageParser.LCB)
            self.state = 308
            self.match(GraphQueryLanguageParser.INT)
            self.state = 309
            self.match(GraphQueryLanguageParser.COLON)
            self.state = 310
            self.match(GraphQueryLanguageParser.INT)
            self.state = 311
            self.match(GraphQueryLanguageParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CfgContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CFG(self):
            return self.getToken(GraphQueryLanguageParser.CFG, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_cfg

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCfg"):
                listener.enterCfg(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCfg"):
                listener.exitCfg(self)

    def cfg(self):

        localctx = GraphQueryLanguageParser.CfgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_cfg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(GraphQueryLanguageParser.CFG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(GraphQueryLanguageParser.STRING, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_string

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterString"):
                listener.enterString(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitString"):
                listener.exitString(self)

    def string(self):

        localctx = GraphQueryLanguageParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(GraphQueryLanguageParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PATH(self):
            return self.getToken(GraphQueryLanguageParser.PATH, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_path

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPath"):
                listener.enterPath(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPath"):
                listener.exitPath(self)

    def path(self):

        localctx = GraphQueryLanguageParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(GraphQueryLanguageParser.PATH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Vertices_setContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(GraphQueryLanguageParser.LCB, 0)

        def RCB(self):
            return self.getToken(GraphQueryLanguageParser.RCB, 0)

        def INT(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.INT)
            else:
                return self.getToken(GraphQueryLanguageParser.INT, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.COMMA)
            else:
                return self.getToken(GraphQueryLanguageParser.COMMA, i)

        def vertices_range(self):
            return self.getTypedRuleContext(
                GraphQueryLanguageParser.Vertices_rangeContext, 0
            )

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_vertices_set

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVertices_set"):
                listener.enterVertices_set(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVertices_set"):
                listener.exitVertices_set(self)

    def vertices_set(self):

        localctx = GraphQueryLanguageParser.Vertices_setContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 56, self.RULE_vertices_set)
        self._la = 0  # Token type
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 32, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(GraphQueryLanguageParser.LCB)
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 30, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 320
                        self.match(GraphQueryLanguageParser.INT)
                        self.state = 321
                        self.match(GraphQueryLanguageParser.COMMA)
                    self.state = 326
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 30, self._ctx)

                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GraphQueryLanguageParser.INT:
                    self.state = 327
                    self.match(GraphQueryLanguageParser.INT)

                self.state = 330
                self.match(GraphQueryLanguageParser.RCB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.vertices_range()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Labels_setContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(GraphQueryLanguageParser.LCB, 0)

        def RCB(self):
            return self.getToken(GraphQueryLanguageParser.RCB, 0)

        def STRING(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.STRING)
            else:
                return self.getToken(GraphQueryLanguageParser.STRING, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.COMMA)
            else:
                return self.getToken(GraphQueryLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_labels_set

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLabels_set"):
                listener.enterLabels_set(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLabels_set"):
                listener.exitLabels_set(self)

    def labels_set(self):

        localctx = GraphQueryLanguageParser.Labels_setContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 58, self.RULE_labels_set)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(GraphQueryLanguageParser.LCB)
            self.state = 339
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 33, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 335
                    self.match(GraphQueryLanguageParser.STRING)
                    self.state = 336
                    self.match(GraphQueryLanguageParser.COMMA)
                self.state = 341
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 33, self._ctx)

            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == GraphQueryLanguageParser.STRING:
                self.state = 342
                self.match(GraphQueryLanguageParser.STRING)

            self.state = 345
            self.match(GraphQueryLanguageParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Edges_setContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(GraphQueryLanguageParser.LCB, 0)

        def RCB(self):
            return self.getToken(GraphQueryLanguageParser.RCB, 0)

        def edge(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryLanguageParser.EdgeContext)
            else:
                return self.getTypedRuleContext(GraphQueryLanguageParser.EdgeContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.COMMA)
            else:
                return self.getToken(GraphQueryLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_edges_set

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEdges_set"):
                listener.enterEdges_set(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEdges_set"):
                listener.exitEdges_set(self)

    def edges_set(self):

        localctx = GraphQueryLanguageParser.Edges_setContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 60, self.RULE_edges_set)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(GraphQueryLanguageParser.LCB)
            self.state = 353
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 35, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 348
                    self.edge()
                    self.state = 349
                    self.match(GraphQueryLanguageParser.COMMA)
                self.state = 355
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 35, self._ctx)

            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == GraphQueryLanguageParser.LP:
                self.state = 356
                self.edge()

            self.state = 359
            self.match(GraphQueryLanguageParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GraphQueryLanguageParser.VAR, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_var

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVar"):
                listener.enterVar(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVar"):
                listener.exitVar(self)

    def var(self):

        localctx = GraphQueryLanguageParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(GraphQueryLanguageParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_edgeContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.LP)
            else:
                return self.getToken(GraphQueryLanguageParser.LP, i)

        def var(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryLanguageParser.VarContext)
            else:
                return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.COMMA)
            else:
                return self.getToken(GraphQueryLanguageParser.COMMA, i)

        def RP(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.RP)
            else:
                return self.getToken(GraphQueryLanguageParser.RP, i)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_var_edge

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVar_edge"):
                listener.enterVar_edge(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVar_edge"):
                listener.exitVar_edge(self)

    def var_edge(self):

        localctx = GraphQueryLanguageParser.Var_edgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_var_edge)
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 37, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(GraphQueryLanguageParser.LP)
                self.state = 364
                self.var()
                self.state = 365
                self.match(GraphQueryLanguageParser.COMMA)
                self.state = 366
                self.var()
                self.state = 367
                self.match(GraphQueryLanguageParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.match(GraphQueryLanguageParser.LP)
                self.state = 370
                self.var()
                self.state = 371
                self.match(GraphQueryLanguageParser.COMMA)
                self.state = 372
                self.var()
                self.state = 373
                self.match(GraphQueryLanguageParser.COMMA)
                self.state = 374
                self.var()
                self.state = 375
                self.match(GraphQueryLanguageParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.match(GraphQueryLanguageParser.LP)
                self.state = 378
                self.match(GraphQueryLanguageParser.LP)
                self.state = 379
                self.var()
                self.state = 380
                self.match(GraphQueryLanguageParser.COMMA)
                self.state = 381
                self.var()
                self.state = 382
                self.match(GraphQueryLanguageParser.RP)
                self.state = 383
                self.match(GraphQueryLanguageParser.COMMA)
                self.state = 384
                self.var()
                self.state = 385
                self.match(GraphQueryLanguageParser.COMMA)
                self.state = 386
                self.match(GraphQueryLanguageParser.LP)
                self.state = 387
                self.var()
                self.state = 388
                self.match(GraphQueryLanguageParser.COMMA)
                self.state = 389
                self.var()
                self.state = 390
                self.match(GraphQueryLanguageParser.RP)
                self.state = 391
                self.match(GraphQueryLanguageParser.RP)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariablesContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueryLanguageParser.VarContext)
            else:
                return self.getTypedRuleContext(GraphQueryLanguageParser.VarContext, i)

        def COMMA(self, i: int = None):
            if i is None:
                return self.getTokens(GraphQueryLanguageParser.COMMA)
            else:
                return self.getToken(GraphQueryLanguageParser.COMMA, i)

        def var_edge(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.Var_edgeContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_variables

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVariables"):
                listener.enterVariables(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVariables"):
                listener.exitVariables(self)

    def variables(self):

        localctx = GraphQueryLanguageParser.VariablesContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 66, self.RULE_variables)
        self._la = 0  # Token type
        try:
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [
                GraphQueryLanguageParser.DOUBLE_ARROW,
                GraphQueryLanguageParser.VAR,
            ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 38, self._ctx)
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 395
                        self.var()
                        self.state = 396
                        self.match(GraphQueryLanguageParser.COMMA)
                    self.state = 402
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 38, self._ctx)

                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == GraphQueryLanguageParser.VAR:
                    self.state = 403
                    self.var()

                pass
            elif token in [GraphQueryLanguageParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.var_edge()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.BooleanContext, 0)

        def graph(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.GraphContext, 0)

        def edges(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.EdgesContext, 0)

        def labels(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.LabelsContext, 0)

        def vertices(self):
            return self.getTypedRuleContext(GraphQueryLanguageParser.VerticesContext, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_val

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVal"):
                listener.enterVal(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVal"):
                listener.exitVal(self)

    def val(self):

        localctx = GraphQueryLanguageParser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_val)
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 41, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.boolean()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.graph()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.edges()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
                self.labels()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 413
                self.vertices()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BooleanContext(ParserRuleContext):
        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(GraphQueryLanguageParser.BOOL, 0)

        def getRuleIndex(self):
            return GraphQueryLanguageParser.RULE_boolean

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBoolean"):
                listener.enterBoolean(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBoolean"):
                listener.exitBoolean(self)

    def boolean(self):

        localctx = GraphQueryLanguageParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_boolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(GraphQueryLanguageParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx: ExprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 5)

        if predIndex == 1:
            return self.precpred(self._ctx, 4)

        if predIndex == 2:
            return self.precpred(self._ctx, 3)

        if predIndex == 3:
            return self.precpred(self._ctx, 2)

        if predIndex == 4:
            return self.precpred(self._ctx, 1)
