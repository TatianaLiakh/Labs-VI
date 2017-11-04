/* FILE OF PROC-IMAGES OF THE PROJECT */
#include "lp10ext.inc" /* Common files for all generated c-files */
#include "lp10xvar.h"  /* Var-images */

void P0 (void) /* ПРОЦЕСС: Инициализация */
{
	switch (Check_State(0)) {

		case 0:    /*  P0S0() - СОСТОЯНИЕ: Начало */
  
  P0V5[1]           = C_1; 
  P0V4[1]        = C_1;
  P0V3[1] = C_0;
  Set_Start(1);    
  Set_Start(2); 
  Set_Stop(0);
			break;
		default:
			break;
	}
}

void P1 (void) /* ПРОЦЕСС: СортировкаЯщиков */
{
	switch (Check_State(1)) {

		case 0:    /*  P1S0() - СОСТОЯНИЕ: Начало */

   if (P0V0 && !P0V1&& !P0V2) { 
       P0V5[1]           = C_0;
       P0V4[1]        = C_1;
	 P0V3[1] = C_1;
   } else {
       P0V5[1]    = C_1;
   }
   if (P0V0 && P0V1) {
	 P0V5[1]           = C_1;
       P0V4[1]        = C_1;
 	 P0V3[1] = C_0;
   }
   if (P0V0 && P0V2) {
	 P0V5[1]           = C_1;
       P0V4[1]        = C_0;
 	 P0V3[1] = C_0;
   }

   
			break;
		default:
			break;
	}
}

void P2 (void) /* ПРОЦЕСС: ПодачаЯщиков */
{
	switch (Check_State(2)) {

		case 0:    /*  P2S0() - СОСТОЯНИЕ: Начало */

   if (!P0V0) { 
       P0V3[1] = C_0;       
   } 
   
			break;
		default:
			break;
	}
}
