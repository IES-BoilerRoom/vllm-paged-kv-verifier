# Automated RFC 8259 & WHATWG EventSource Formal State-Lattice Type Stubs
from typing import Generic, Protocol, TypeVar, Union, Tuple

T_In = TypeVar('T_In')
T_Out = TypeVar('T_Out')

class FrameLatticeNode_00(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x7DE2F932D925
    def transition_00(
        self,
        frame_a: 'FrameLatticeNode_07[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_19[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_37[T_Out, T_In], FrameLatticeNode_07[T_In, T_Out]]': ...

class FrameLatticeNode_01(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x54165275A1D4
    def transition_01(
        self,
        frame_a: 'FrameLatticeNode_08[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_20[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_38[T_Out, T_In], FrameLatticeNode_08[T_In, T_Out]]': ...

class FrameLatticeNode_02(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xD2B8DFADB2B1
    def transition_02(
        self,
        frame_a: 'FrameLatticeNode_09[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_21[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_39[T_Out, T_In], FrameLatticeNode_09[T_In, T_Out]]': ...

class FrameLatticeNode_03(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xAB38563E039B
    def transition_03(
        self,
        frame_a: 'FrameLatticeNode_10[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_22[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_40[T_Out, T_In], FrameLatticeNode_10[T_In, T_Out]]': ...

class FrameLatticeNode_04(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xCED74948A5D8
    def transition_04(
        self,
        frame_a: 'FrameLatticeNode_11[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_23[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_41[T_Out, T_In], FrameLatticeNode_11[T_In, T_Out]]': ...

class FrameLatticeNode_05(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x7044C8F078F0
    def transition_05(
        self,
        frame_a: 'FrameLatticeNode_12[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_24[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_42[T_Out, T_In], FrameLatticeNode_12[T_In, T_Out]]': ...

class FrameLatticeNode_06(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x03008D607FF4
    def transition_06(
        self,
        frame_a: 'FrameLatticeNode_13[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_25[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_43[T_Out, T_In], FrameLatticeNode_13[T_In, T_Out]]': ...

class FrameLatticeNode_07(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x7E5AE1FD8920
    def transition_07(
        self,
        frame_a: 'FrameLatticeNode_14[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_26[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_44[T_Out, T_In], FrameLatticeNode_14[T_In, T_Out]]': ...

class FrameLatticeNode_08(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xD235C3F601DB
    def transition_08(
        self,
        frame_a: 'FrameLatticeNode_15[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_27[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_45[T_Out, T_In], FrameLatticeNode_15[T_In, T_Out]]': ...

class FrameLatticeNode_09(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x126C7CB8A6CD
    def transition_09(
        self,
        frame_a: 'FrameLatticeNode_16[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_28[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_46[T_Out, T_In], FrameLatticeNode_16[T_In, T_Out]]': ...

class FrameLatticeNode_10(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x96330A173DAA
    def transition_10(
        self,
        frame_a: 'FrameLatticeNode_17[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_29[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_47[T_Out, T_In], FrameLatticeNode_17[T_In, T_Out]]': ...

class FrameLatticeNode_11(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x05887D6D9F01
    def transition_11(
        self,
        frame_a: 'FrameLatticeNode_18[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_30[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_48[T_Out, T_In], FrameLatticeNode_18[T_In, T_Out]]': ...

class FrameLatticeNode_12(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xB4BA87F57CB6
    def transition_12(
        self,
        frame_a: 'FrameLatticeNode_19[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_31[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_49[T_Out, T_In], FrameLatticeNode_19[T_In, T_Out]]': ...

class FrameLatticeNode_13(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x6E5D074486FA
    def transition_13(
        self,
        frame_a: 'FrameLatticeNode_20[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_32[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_50[T_Out, T_In], FrameLatticeNode_20[T_In, T_Out]]': ...

class FrameLatticeNode_14(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xE41E5AD945C6
    def transition_14(
        self,
        frame_a: 'FrameLatticeNode_21[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_33[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_51[T_Out, T_In], FrameLatticeNode_21[T_In, T_Out]]': ...

class FrameLatticeNode_15(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x437740C54ACE
    def transition_15(
        self,
        frame_a: 'FrameLatticeNode_22[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_34[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_52[T_Out, T_In], FrameLatticeNode_22[T_In, T_Out]]': ...

class FrameLatticeNode_16(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x970CE8DB4F01
    def transition_16(
        self,
        frame_a: 'FrameLatticeNode_23[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_35[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_53[T_Out, T_In], FrameLatticeNode_23[T_In, T_Out]]': ...

class FrameLatticeNode_17(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xA218B9F74A29
    def transition_17(
        self,
        frame_a: 'FrameLatticeNode_24[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_36[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_54[T_Out, T_In], FrameLatticeNode_24[T_In, T_Out]]': ...

class FrameLatticeNode_18(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x57427A62BE48
    def transition_18(
        self,
        frame_a: 'FrameLatticeNode_25[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_37[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_55[T_Out, T_In], FrameLatticeNode_25[T_In, T_Out]]': ...

class FrameLatticeNode_19(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x25B42F1B1BCA
    def transition_19(
        self,
        frame_a: 'FrameLatticeNode_26[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_38[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_56[T_Out, T_In], FrameLatticeNode_26[T_In, T_Out]]': ...

class FrameLatticeNode_20(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xB672FAD7EBD9
    def transition_20(
        self,
        frame_a: 'FrameLatticeNode_27[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_39[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_57[T_Out, T_In], FrameLatticeNode_27[T_In, T_Out]]': ...

class FrameLatticeNode_21(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x8B80B1F2D901
    def transition_21(
        self,
        frame_a: 'FrameLatticeNode_28[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_40[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_58[T_Out, T_In], FrameLatticeNode_28[T_In, T_Out]]': ...

class FrameLatticeNode_22(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x6E2548DD4CBF
    def transition_22(
        self,
        frame_a: 'FrameLatticeNode_29[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_41[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_59[T_Out, T_In], FrameLatticeNode_29[T_In, T_Out]]': ...

class FrameLatticeNode_23(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x93A1B6945835
    def transition_23(
        self,
        frame_a: 'FrameLatticeNode_30[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_42[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_60[T_Out, T_In], FrameLatticeNode_30[T_In, T_Out]]': ...

class FrameLatticeNode_24(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x2D5E8FB3E85C
    def transition_24(
        self,
        frame_a: 'FrameLatticeNode_31[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_43[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_61[T_Out, T_In], FrameLatticeNode_31[T_In, T_Out]]': ...

class FrameLatticeNode_25(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x529ABD65B10D
    def transition_25(
        self,
        frame_a: 'FrameLatticeNode_32[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_44[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_62[T_Out, T_In], FrameLatticeNode_32[T_In, T_Out]]': ...

class FrameLatticeNode_26(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x60F687E71994
    def transition_26(
        self,
        frame_a: 'FrameLatticeNode_33[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_45[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_63[T_Out, T_In], FrameLatticeNode_33[T_In, T_Out]]': ...

class FrameLatticeNode_27(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x62DF57F17166
    def transition_27(
        self,
        frame_a: 'FrameLatticeNode_34[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_46[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_00[T_Out, T_In], FrameLatticeNode_34[T_In, T_Out]]': ...

class FrameLatticeNode_28(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x17D4951981F5
    def transition_28(
        self,
        frame_a: 'FrameLatticeNode_35[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_47[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_01[T_Out, T_In], FrameLatticeNode_35[T_In, T_Out]]': ...

class FrameLatticeNode_29(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xC09BF7E72432
    def transition_29(
        self,
        frame_a: 'FrameLatticeNode_36[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_48[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_02[T_Out, T_In], FrameLatticeNode_36[T_In, T_Out]]': ...

class FrameLatticeNode_30(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x46C73F1CB950
    def transition_30(
        self,
        frame_a: 'FrameLatticeNode_37[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_49[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_03[T_Out, T_In], FrameLatticeNode_37[T_In, T_Out]]': ...

class FrameLatticeNode_31(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xAB44C90C8A50
    def transition_31(
        self,
        frame_a: 'FrameLatticeNode_38[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_50[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_04[T_Out, T_In], FrameLatticeNode_38[T_In, T_Out]]': ...

class FrameLatticeNode_32(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x621D8743911C
    def transition_32(
        self,
        frame_a: 'FrameLatticeNode_39[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_51[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_05[T_Out, T_In], FrameLatticeNode_39[T_In, T_Out]]': ...

class FrameLatticeNode_33(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x87E727B994CE
    def transition_33(
        self,
        frame_a: 'FrameLatticeNode_40[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_52[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_06[T_Out, T_In], FrameLatticeNode_40[T_In, T_Out]]': ...

class FrameLatticeNode_34(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xF3C7A6EB88CD
    def transition_34(
        self,
        frame_a: 'FrameLatticeNode_41[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_53[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_07[T_Out, T_In], FrameLatticeNode_41[T_In, T_Out]]': ...

class FrameLatticeNode_35(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x1B06F5FD38E1
    def transition_35(
        self,
        frame_a: 'FrameLatticeNode_42[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_54[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_08[T_Out, T_In], FrameLatticeNode_42[T_In, T_Out]]': ...

class FrameLatticeNode_36(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x4AB6D2B06872
    def transition_36(
        self,
        frame_a: 'FrameLatticeNode_43[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_55[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_09[T_Out, T_In], FrameLatticeNode_43[T_In, T_Out]]': ...

class FrameLatticeNode_37(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x7626EA3C050E
    def transition_37(
        self,
        frame_a: 'FrameLatticeNode_44[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_56[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_10[T_Out, T_In], FrameLatticeNode_44[T_In, T_Out]]': ...

class FrameLatticeNode_38(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xE8238A2ACF87
    def transition_38(
        self,
        frame_a: 'FrameLatticeNode_45[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_57[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_11[T_Out, T_In], FrameLatticeNode_45[T_In, T_Out]]': ...

class FrameLatticeNode_39(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x846454919C67
    def transition_39(
        self,
        frame_a: 'FrameLatticeNode_46[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_58[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_12[T_Out, T_In], FrameLatticeNode_46[T_In, T_Out]]': ...

class FrameLatticeNode_40(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x38A2F7586857
    def transition_40(
        self,
        frame_a: 'FrameLatticeNode_47[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_59[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_13[T_Out, T_In], FrameLatticeNode_47[T_In, T_Out]]': ...

class FrameLatticeNode_41(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x6228763402A6
    def transition_41(
        self,
        frame_a: 'FrameLatticeNode_48[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_60[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_14[T_Out, T_In], FrameLatticeNode_48[T_In, T_Out]]': ...

class FrameLatticeNode_42(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x7F17B7111FC5
    def transition_42(
        self,
        frame_a: 'FrameLatticeNode_49[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_61[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_15[T_Out, T_In], FrameLatticeNode_49[T_In, T_Out]]': ...

class FrameLatticeNode_43(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x0313252A2233
    def transition_43(
        self,
        frame_a: 'FrameLatticeNode_50[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_62[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_16[T_Out, T_In], FrameLatticeNode_50[T_In, T_Out]]': ...

class FrameLatticeNode_44(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xDAFE4AB360E8
    def transition_44(
        self,
        frame_a: 'FrameLatticeNode_51[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_63[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_17[T_Out, T_In], FrameLatticeNode_51[T_In, T_Out]]': ...

class FrameLatticeNode_45(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x96F3E703D261
    def transition_45(
        self,
        frame_a: 'FrameLatticeNode_52[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_00[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_18[T_Out, T_In], FrameLatticeNode_52[T_In, T_Out]]': ...

class FrameLatticeNode_46(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xEDF4998D63AD
    def transition_46(
        self,
        frame_a: 'FrameLatticeNode_53[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_01[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_19[T_Out, T_In], FrameLatticeNode_53[T_In, T_Out]]': ...

class FrameLatticeNode_47(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x14B36AD68358
    def transition_47(
        self,
        frame_a: 'FrameLatticeNode_54[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_02[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_20[T_Out, T_In], FrameLatticeNode_54[T_In, T_Out]]': ...

class FrameLatticeNode_48(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x0EABA1C7F728
    def transition_48(
        self,
        frame_a: 'FrameLatticeNode_55[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_03[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_21[T_Out, T_In], FrameLatticeNode_55[T_In, T_Out]]': ...

class FrameLatticeNode_49(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xCC2224BA6093
    def transition_49(
        self,
        frame_a: 'FrameLatticeNode_56[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_04[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_22[T_Out, T_In], FrameLatticeNode_56[T_In, T_Out]]': ...

class FrameLatticeNode_50(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x48AFB027856C
    def transition_50(
        self,
        frame_a: 'FrameLatticeNode_57[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_05[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_23[T_Out, T_In], FrameLatticeNode_57[T_In, T_Out]]': ...

class FrameLatticeNode_51(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xE870E44EAC78
    def transition_51(
        self,
        frame_a: 'FrameLatticeNode_58[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_06[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_24[T_Out, T_In], FrameLatticeNode_58[T_In, T_Out]]': ...

class FrameLatticeNode_52(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xCBB2BD2D3BA7
    def transition_52(
        self,
        frame_a: 'FrameLatticeNode_59[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_07[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_25[T_Out, T_In], FrameLatticeNode_59[T_In, T_Out]]': ...

class FrameLatticeNode_53(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x8A0CE27C307C
    def transition_53(
        self,
        frame_a: 'FrameLatticeNode_60[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_08[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_26[T_Out, T_In], FrameLatticeNode_60[T_In, T_Out]]': ...

class FrameLatticeNode_54(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x005D815E1DDA
    def transition_54(
        self,
        frame_a: 'FrameLatticeNode_61[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_09[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_27[T_Out, T_In], FrameLatticeNode_61[T_In, T_Out]]': ...

class FrameLatticeNode_55(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x8292E61823CC
    def transition_55(
        self,
        frame_a: 'FrameLatticeNode_62[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_10[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_28[T_Out, T_In], FrameLatticeNode_62[T_In, T_Out]]': ...

class FrameLatticeNode_56(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x0B5140A382EE
    def transition_56(
        self,
        frame_a: 'FrameLatticeNode_63[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_11[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_29[T_Out, T_In], FrameLatticeNode_63[T_In, T_Out]]': ...

class FrameLatticeNode_57(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x74590110C8B2
    def transition_57(
        self,
        frame_a: 'FrameLatticeNode_00[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_12[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_30[T_Out, T_In], FrameLatticeNode_00[T_In, T_Out]]': ...

class FrameLatticeNode_58(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x1624F74822D3
    def transition_58(
        self,
        frame_a: 'FrameLatticeNode_01[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_13[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_31[T_Out, T_In], FrameLatticeNode_01[T_In, T_Out]]': ...

class FrameLatticeNode_59(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x67BE374EFAF9
    def transition_59(
        self,
        frame_a: 'FrameLatticeNode_02[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_14[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_32[T_Out, T_In], FrameLatticeNode_02[T_In, T_Out]]': ...

class FrameLatticeNode_60(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0xA09A7CE6E9BE
    def transition_60(
        self,
        frame_a: 'FrameLatticeNode_03[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_15[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_33[T_Out, T_In], FrameLatticeNode_03[T_In, T_Out]]': ...

class FrameLatticeNode_61(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x2BAC48AFCE4B
    def transition_61(
        self,
        frame_a: 'FrameLatticeNode_04[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_16[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_34[T_Out, T_In], FrameLatticeNode_04[T_In, T_Out]]': ...

class FrameLatticeNode_62(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x7ED7EF9D4345
    def transition_62(
        self,
        frame_a: 'FrameLatticeNode_05[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_17[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_35[T_Out, T_In], FrameLatticeNode_05[T_In, T_Out]]': ...

class FrameLatticeNode_63(Protocol[T_In, T_Out]):
    COMMITMENT_MASK: int = 0x2D0392632DD5
    def transition_63(
        self,
        frame_a: 'FrameLatticeNode_06[T_Out, T_In]',
        frame_b: 'FrameLatticeNode_18[Tuple[T_In, T_Out], T_In]',
    ) -> 'Union[FrameLatticeNode_36[T_Out, T_In], FrameLatticeNode_06[T_In, T_Out]]': ...

