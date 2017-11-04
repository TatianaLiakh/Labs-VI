#include "R_CNST.h"
#include "R_IO.h"
#include "axvar.h"
void Output (void)
{
	if (P0V10[0] != P0V10[1]) {
		FPO0 = ON;
		if (!(P0V10[1] == ZERO)) PO0 |= MASK1_S8;
		else PO0 &= ~MASK1_S8;
	}
	if (P0V11[0] != P0V11[1]) {
		FPO0 = ON;
		if (!(P0V11[1] == ZERO)) PO0 |= MASK2_S8;
		else PO0 &= ~MASK2_S8;
	}
	if (P0V12[0] != P0V12[1]) {
		FPO0 = ON;
		if (!(P0V12[1] == ZERO)) PO0 |= MASK3_S8;
		else PO0 &= ~MASK3_S8;
	}
	if (P0V13[0] != P0V13[1]) {
		FPO0 = ON;
		if (!(P0V13[1] == ZERO)) PO0 |= MASK4_S8;
		else PO0 &= ~MASK4_S8;
	}
	if (P0V14[0] != P0V14[1]) {
		FPO0 = ON;
		if (!(P0V14[1] == ZERO)) PO0 |= MASK5_S8;
		else PO0 &= ~MASK5_S8;
	}
	if (P0V15[0] != P0V15[1]) {
		FPO0 = ON;
		if (!(P0V15[1] == ZERO)) PO0 |= MASK6_S8;
		else PO0 &= ~MASK6_S8;
	}
	if (P0V16[0] != P0V16[1]) {
		FPO1 = ON;
		if (!(P0V16[1] == ZERO)) PO1 |= MASK1_S8;
		else PO1 &= ~MASK1_S8;
	}
	if (P0V17[0] != P0V17[1]) {
		FPO1 = ON;
		if (!(P0V17[1] == ZERO)) PO1 |= MASK2_S8;
		else PO1 &= ~MASK2_S8;
	}
	if (P0V18[0] != P0V18[1]) {
		FPO1 = ON;
		if (!(P0V18[1] == ZERO)) PO1 |= MASK3_S8;
		else PO1 &= ~MASK3_S8;
	}


/*======= Output Port =============*/
	if(FPO0 == ON) OUTBYTE((INT16U)0, (INT16U)0, (INT8U)~PO0);
	if(FPO1 == ON) OUTBYTE((INT16U)1, (INT16U)0, (INT8U)~PO1);
}
