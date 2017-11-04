#include "R_CNST.h"
#include "R_IO.h"
#include "lp10xvar.h"
void Input (void)
{
/*======= Input Ports Reading =============*/
	PI0 = INBYTE((INT16U)0, (INT16U)0); /* чтение байта */
	FPO0 = OFF; PO0 = ~INBYTE((INT16U)0, (INT16U)0);
	if (PI0 & MASK1_S8) P0V0 = 1;
	else P0V0 = 0;
	if (PI0 & MASK2_S8) P0V1 = 1;
	else P0V1 = 0;
	if (PI0 & MASK3_S8) P0V2 = 1;
	else P0V2 = 0;
	if (PO0 & MASK1_S8) P0V3[0] = 1;
	else P0V3[0] = 0;
	P0V3[1] = P0V3[0];
	if (PO0 & MASK2_S8) P0V4[0] = 1;
	else P0V4[0] = 0;
	P0V4[1] = P0V4[0];
	if (PO0 & MASK3_S8) P0V5[0] = 1;
	else P0V5[0] = 0;
	P0V5[1] = P0V5[0];
}
