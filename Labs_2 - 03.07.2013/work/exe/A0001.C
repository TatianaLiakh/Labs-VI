/* FILE OF PROC-IMAGES OF THE PROJECT */
#include "aext.inc" /* Common files for all generated c-files */
#include "axvar.h"  /* Var-images */

void P0 (void) /* ПРОЦЕСС: Инициализация */
{
	switch (Check_State(0)) {

		case 0:    /*  P0S0() - СОСТОЯНИЕ: Начало */
  
P0V10[1] = C_1; 
P0V11[1]  = C_1;
Set_Start(1); 
Set_Stop(0);
			break;
		default:
			break;
	}
}

void P1 (void) /* ПРОЦЕСС: Щебень */
{
	switch (Check_State(1)) {

		case 0:    /*  P1S0() - СОСТОЯНИЕ: Начало */

      if (P0V7 == 0 ) {
       P0V10[1] = C_0;
  } else
 P0V10[1] = C_1;  
   
			break;
		default:
			break;
	}
}
