#include "R_CNST.h"
#include "R_IO.h"
#include "lp10xvar.h"
void Output (void)
{
	if (P0V3[0] != P0V3[1]) {
		FPO0 = ON;
		if (!(P0V3[1] == ZERO)) PO0 |= MASK1_S8;
		else PO0 &= ~MASK1_S8;
	}
	if (P0V4[0] != P0V4[1]) {
		FPO0 = ON;
		if (!(P0V4[1] == ZERO)) PO0 |= MASK2_S8;
		else PO0 &= ~MASK2_S8;
	}
	if (P0V5[0] != P0V5[1]) {
		FPO0 = ON;
		if (!(P0V5[1] == ZERO)) PO0 |= MASK3_S8;
		else PO0 &= ~MASK3_S8;
	}


/*======= Output Port =============*/
	if(FPO0 == ON) OUTBYTE((INT16U)0, (INT16U)0, (INT8U)~PO0);
}
