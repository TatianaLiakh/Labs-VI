########################################
# in[], out[] -> âíóòğåííèå ïåğåìåííûå #
########################################

P0V0 = 0;
if (inputdata[0] & 1):	P0V0 = 1;

P0V1 = 0;
if (inputdata[0] & 2):	P0V1 = 1;

P0V2 = 0;
if (inputdata[0] & 4):	P0V2 = 1;

P0V3 = 0;
if (inputdata[0] & 8):	P0V3 = 1;

P0V4 = 0;
if (inputdata[0] & 16):	P0V4 = 1;

P0V5 = 0;
if (inputdata[0] & 32):	P0V5 = 1;

P0V6 = 0;
if (inputdata[0] & 64):	P0V6 = 1;

P0V7 = 0;
if (inputdata[1] & 1):	P0V7 = 1;

P0V8 = 0;
if (inputdata[1] & 2):	P0V8 = 1;

P0V9 = 0;
if (inputdata[1] & 4):	P0V9 = 1;

P0V10 = [0,0];
if (outputdata[0] & 1):
	P0V10[0] = 1;
P0V10[1] = P0V10[0];

P0V11 = [0,0];
if (outputdata[0] & 2):
	P0V11[0] = 1;
P0V11[1] = P0V11[0];

P0V12 = [0,0];
if (outputdata[0] & 4):
	P0V12[0] = 1;
P0V12[1] = P0V12[0];

P0V13 = [0,0];
if (outputdata[0] & 8):
	P0V13[0] = 1;
P0V13[1] = P0V13[0];

P0V14 = [0,0];
if (outputdata[0] & 16):
	P0V14[0] = 1;
P0V14[1] = P0V14[0];

P0V15 = [0,0];
if (outputdata[0] & 32):
	P0V15[0] = 1;
P0V15[1] = P0V15[0];

P0V16 = [0,0];
if (outputdata[1] & 1):
	P0V16[0] = 1;
P0V16[1] = P0V16[0];

P0V17 = [0,0];
if (outputdata[1] & 2):
	P0V17[0] = 1;
P0V17[1] = P0V17[0];

P0V18 = [0,0];
if (outputdata[1] & 4):
	P0V18[0] = 1;
P0V18[1] = P0V18[0];

########################################
######### = ÒÅËÎ ÏĞÎÃĞÀÌÌÛ = ###########
########################################
 
C_0 =  1; 
C_1 =  0;
i = 0;
while i < 2:
	times[i] += 1; i +=1;

# ÏĞÎÖÅÑÑ Èíèöèàëèçàöèÿ (# 0)
cur_state_copy = states[0];
if(cur_state_copy == 0):    #  ÑÎÑÒÎßÍÈÅ: Íà÷àëî (P0S0)
	P0V10[1] = C_1;
	P0V11[1] = C_1; 
	states[1] = 0; times [1] = 0; # ÑÒÀĞÒ
	states[0] = 255; # STOP

# ÏĞÎÖÅÑÑ Ùåáåíü (# 1)
cur_state_copy = states[1];
if(cur_state_copy == 0):    #  ÑÎÑÒÎßÍÈÅ: Íà÷àëî (P0S1)
	if(P0V7 == 0 ) : 
		P0V10[1] = C_0;  
	else :
		P0V10[1] = C_1; 

##################################
# âíóòğåííèå ïåğåìåííûå -> out[] #
##################################

if (P0V10[0] != P0V10[1]):
	if (P0V10[1] != 0):
		outputdata[0] |= 1;
	else:
		outputdata[0] &= ~1;

if (P0V11[0] != P0V11[1]):
	if (P0V11[1] != 0):
		outputdata[0] |= 2;
	else:
		outputdata[0] &= ~2;

if (P0V12[0] != P0V12[1]):
	if (P0V12[1] != 0):
		outputdata[0] |= 4;
	else:
		outputdata[0] &= ~4;

if (P0V13[0] != P0V13[1]):
	if (P0V13[1] != 0):
		outputdata[0] |= 8;
	else:
		outputdata[0] &= ~8;

if (P0V14[0] != P0V14[1]):
	if (P0V14[1] != 0):
		outputdata[0] |= 16;
	else:
		outputdata[0] &= ~16;

if (P0V15[0] != P0V15[1]):
	if (P0V15[1] != 0):
		outputdata[0] |= 32;
	else:
		outputdata[0] &= ~32;

if (P0V16[0] != P0V16[1]):
	if (P0V16[1] != 0):
		outputdata[1] |= 1;
	else:
		outputdata[1] &= ~1;

if (P0V17[0] != P0V17[1]):
	if (P0V17[1] != 0):
		outputdata[1] |= 2;
	else:
		outputdata[1] &= ~2;

if (P0V18[0] != P0V18[1]):
	if (P0V18[1] != 0):
		outputdata[1] |= 4;
	else:
		outputdata[1] &= ~4;