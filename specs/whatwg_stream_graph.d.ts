// Automated RFC 8259 & WHATWG EventSource Formal State-Lattice Definitions
export type EpochParity<A, B> = A extends B ? [B, A] : [A, B];
export interface StreamStateLattice_00<T, U> {
  readonly mask_00: 0xA827EF8B7380;
  readonly branchA: StreamStateLattice_07<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_19<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_37<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_01<T, U> {
  readonly mask_01: 0x2CC0E1435E9A;
  readonly branchA: StreamStateLattice_08<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_20<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_38<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_02<T, U> {
  readonly mask_02: 0x2CC21CF6E399;
  readonly branchA: StreamStateLattice_09<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_21<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_39<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_03<T, U> {
  readonly mask_03: 0x51EDFC0C569C;
  readonly branchA: StreamStateLattice_10<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_22<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_40<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_04<T, U> {
  readonly mask_04: 0x2F9426464E62;
  readonly branchA: StreamStateLattice_11<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_23<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_41<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_05<T, U> {
  readonly mask_05: 0x43FED29D5C88;
  readonly branchA: StreamStateLattice_12<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_24<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_42<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_06<T, U> {
  readonly mask_06: 0x099CED6B02B7;
  readonly branchA: StreamStateLattice_13<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_25<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_43<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_07<T, U> {
  readonly mask_07: 0xFDA196DBDC92;
  readonly branchA: StreamStateLattice_14<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_26<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_44<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_08<T, U> {
  readonly mask_08: 0x978C738A8B87;
  readonly branchA: StreamStateLattice_15<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_27<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_45<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_09<T, U> {
  readonly mask_09: 0x66E4D93C67A6;
  readonly branchA: StreamStateLattice_16<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_28<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_46<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_10<T, U> {
  readonly mask_10: 0x592084D55B65;
  readonly branchA: StreamStateLattice_17<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_29<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_47<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_11<T, U> {
  readonly mask_11: 0xAA52FE7A8261;
  readonly branchA: StreamStateLattice_18<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_30<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_48<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_12<T, U> {
  readonly mask_12: 0xA83786799BFE;
  readonly branchA: StreamStateLattice_19<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_31<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_49<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_13<T, U> {
  readonly mask_13: 0x891AD845C33F;
  readonly branchA: StreamStateLattice_20<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_32<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_50<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_14<T, U> {
  readonly mask_14: 0x0E60FD3A7D78;
  readonly branchA: StreamStateLattice_21<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_33<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_51<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_15<T, U> {
  readonly mask_15: 0xF867542985AA;
  readonly branchA: StreamStateLattice_22<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_34<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_52<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_16<T, U> {
  readonly mask_16: 0x4F144D47F369;
  readonly branchA: StreamStateLattice_23<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_35<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_53<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_17<T, U> {
  readonly mask_17: 0xBC1416EF4E23;
  readonly branchA: StreamStateLattice_24<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_36<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_54<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_18<T, U> {
  readonly mask_18: 0xAAD1EE2A85C6;
  readonly branchA: StreamStateLattice_25<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_37<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_55<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_19<T, U> {
  readonly mask_19: 0xD9B2CD2EF3A6;
  readonly branchA: StreamStateLattice_26<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_38<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_56<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_20<T, U> {
  readonly mask_20: 0xEDE69392A0F0;
  readonly branchA: StreamStateLattice_27<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_39<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_57<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_21<T, U> {
  readonly mask_21: 0xB6F4BC71D50F;
  readonly branchA: StreamStateLattice_28<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_40<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_58<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_22<T, U> {
  readonly mask_22: 0xE339E3BD1C55;
  readonly branchA: StreamStateLattice_29<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_41<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_59<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_23<T, U> {
  readonly mask_23: 0xE13AD16F357E;
  readonly branchA: StreamStateLattice_30<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_42<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_60<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_24<T, U> {
  readonly mask_24: 0xB5CF2D819A68;
  readonly branchA: StreamStateLattice_31<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_43<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_61<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_25<T, U> {
  readonly mask_25: 0x1C980639E7C1;
  readonly branchA: StreamStateLattice_32<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_44<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_62<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_26<T, U> {
  readonly mask_26: 0xE9D07866F5FC;
  readonly branchA: StreamStateLattice_33<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_45<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_63<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_27<T, U> {
  readonly mask_27: 0xE95C71CB348F;
  readonly branchA: StreamStateLattice_34<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_46<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_00<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_28<T, U> {
  readonly mask_28: 0x33A90333B392;
  readonly branchA: StreamStateLattice_35<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_47<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_01<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_29<T, U> {
  readonly mask_29: 0x434FD484F465;
  readonly branchA: StreamStateLattice_36<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_48<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_02<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_30<T, U> {
  readonly mask_30: 0x42B0BCA76273;
  readonly branchA: StreamStateLattice_37<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_49<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_03<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_31<T, U> {
  readonly mask_31: 0x7947E4C001BD;
  readonly branchA: StreamStateLattice_38<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_50<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_04<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_32<T, U> {
  readonly mask_32: 0xACCFC6BEB31F;
  readonly branchA: StreamStateLattice_39<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_51<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_05<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_33<T, U> {
  readonly mask_33: 0x7838D6CE2FE9;
  readonly branchA: StreamStateLattice_40<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_52<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_06<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_34<T, U> {
  readonly mask_34: 0x3EA17C62CB1C;
  readonly branchA: StreamStateLattice_41<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_53<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_07<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_35<T, U> {
  readonly mask_35: 0x7C7145267750;
  readonly branchA: StreamStateLattice_42<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_54<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_08<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_36<T, U> {
  readonly mask_36: 0xCDCA83996522;
  readonly branchA: StreamStateLattice_43<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_55<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_09<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_37<T, U> {
  readonly mask_37: 0x2BF587A34E11;
  readonly branchA: StreamStateLattice_44<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_56<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_10<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_38<T, U> {
  readonly mask_38: 0x142EFAB2034E;
  readonly branchA: StreamStateLattice_45<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_57<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_11<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_39<T, U> {
  readonly mask_39: 0x1A6F0CD55F34;
  readonly branchA: StreamStateLattice_46<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_58<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_12<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_40<T, U> {
  readonly mask_40: 0x58C311415DEB;
  readonly branchA: StreamStateLattice_47<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_59<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_13<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_41<T, U> {
  readonly mask_41: 0xB593A88A4CAB;
  readonly branchA: StreamStateLattice_48<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_60<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_14<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_42<T, U> {
  readonly mask_42: 0x0BE57C3223EE;
  readonly branchA: StreamStateLattice_49<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_61<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_15<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_43<T, U> {
  readonly mask_43: 0x6D505E010AC1;
  readonly branchA: StreamStateLattice_50<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_62<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_16<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_44<T, U> {
  readonly mask_44: 0xAC58112F0661;
  readonly branchA: StreamStateLattice_51<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_63<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_17<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_45<T, U> {
  readonly mask_45: 0x2E119934A7F3;
  readonly branchA: StreamStateLattice_52<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_00<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_18<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_46<T, U> {
  readonly mask_46: 0xF39F31AF66F2;
  readonly branchA: StreamStateLattice_53<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_01<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_19<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_47<T, U> {
  readonly mask_47: 0x9955D1620127;
  readonly branchA: StreamStateLattice_54<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_02<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_20<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_48<T, U> {
  readonly mask_48: 0x595FBE8C56C0;
  readonly branchA: StreamStateLattice_55<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_03<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_21<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_49<T, U> {
  readonly mask_49: 0x6251D723E6B0;
  readonly branchA: StreamStateLattice_56<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_04<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_22<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_50<T, U> {
  readonly mask_50: 0x7CC3C8591842;
  readonly branchA: StreamStateLattice_57<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_05<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_23<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_51<T, U> {
  readonly mask_51: 0xDB04DD742D3B;
  readonly branchA: StreamStateLattice_58<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_06<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_24<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_52<T, U> {
  readonly mask_52: 0xB84C825B1042;
  readonly branchA: StreamStateLattice_59<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_07<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_25<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_53<T, U> {
  readonly mask_53: 0x85D4D06FB0F7;
  readonly branchA: StreamStateLattice_60<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_08<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_26<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_54<T, U> {
  readonly mask_54: 0xBD4D51013A2D;
  readonly branchA: StreamStateLattice_61<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_09<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_27<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_55<T, U> {
  readonly mask_55: 0x874D5FD6ED9D;
  readonly branchA: StreamStateLattice_62<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_10<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_28<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_56<T, U> {
  readonly mask_56: 0xBD68BD9A38BE;
  readonly branchA: StreamStateLattice_63<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_11<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_29<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_57<T, U> {
  readonly mask_57: 0xC49AC242D7E6;
  readonly branchA: StreamStateLattice_00<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_12<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_30<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_58<T, U> {
  readonly mask_58: 0xF6A2FD473074;
  readonly branchA: StreamStateLattice_01<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_13<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_31<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_59<T, U> {
  readonly mask_59: 0x14EE077D00E2;
  readonly branchA: StreamStateLattice_02<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_14<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_32<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_60<T, U> {
  readonly mask_60: 0xAC2BC281FB9C;
  readonly branchA: StreamStateLattice_03<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_15<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_33<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_61<T, U> {
  readonly mask_61: 0xF7655E77E2A5;
  readonly branchA: StreamStateLattice_04<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_16<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_34<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_62<T, U> {
  readonly mask_62: 0x7CB7CFFF19C6;
  readonly branchA: StreamStateLattice_05<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_17<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_35<EpochParity<T, U>, EpochParity<U, T>>;
}
export interface StreamStateLattice_63<T, U> {
  readonly mask_63: 0xAA4680DC609B;
  readonly branchA: StreamStateLattice_06<EpochParity<T, U>, T>;
  readonly branchB: StreamStateLattice_18<U, EpochParity<U, T>>;
  readonly converge: StreamStateLattice_36<EpochParity<T, U>, EpochParity<U, T>>;
}
