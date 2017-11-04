########################################
# in[], out[] -> ���������� ���������� #
########################################

P0V0 = 0;
if (inputdata[0] & 1):	P0V0 = 1;

P0V1 = 0;
if (inputdata[0] & 2):	P0V1 = 1;

P0V2 = 0;
if (inputdata[0] & 4):	P0V2 = 1;

P0V3 = [0,0];
if (outputdata[0] & 1):
	P0V3[0] = 1;
P0V3[1] = P0V3[0];

P0V4 = [0,0];
if (outputdata[0] & 2):
	P0V4[0] = 1;
P0V4[1] = P0V4[0];

P0V5 = [0,0];
if (outputdata[0] & 4):
	P0V5[0] = 1;
P0V5[1] = P0V5[0];

########################################
######### = ���� ��������� = ###########
########################################
 
C_0 =  1; 
C_1 =  0;
i = 0;
while i < 3:
	times[i] += 1; i +=1;

# ������� ������������� (# 0)
cur_state_copy = states[0];
if(cur_state_copy == 0):    #  ���������: ������ (P0S0)
	P0V5[1] = C_1;
	P0V4[1] = C_1;
	P0V3[1] = C_0; 
	states[1] = 0; times [1] = 0; # �����
	states[2] = 0; times [2] = 0; # �����
	states[0] = 255; # STOP

# ������� ���������������� (# 1)
cur_state_copy = states[1];
if(cur_state_copy == 0):    #  ���������: ������ (P0S1)
	if(P0V0  and   not P0V1 and   not P0V2) : 
		P0V5[1] = C_0;
		P0V4[1] = C_1;
		P0V3[1] = C_1;  
	else :
		P0V5[1] = C_1;  
	if(P0V0  and  P0V1) : 
		P0V5[1] = C_1;
		P0V4[1] = C_1;
		P0V3[1] = C_0;  
	if(P0V0  and  P0V2) : 
		P0V5[1] = C_1;
		P0V4[1] = C_0;
		P0V3[1] = C_0;  

# ������� ������������ (# 2)
cur_state_copy = states[2];
if(cur_state_copy == 0):    #  ���������: ������ (P0S2) 
	if( not P0V0) : 
		P0V3[1] = C_0;  

##################################
# ���������� ���������� -> out[] #
##################################

if (P0V3[0] != P0V3[1]):
	if (P0V3[1] != 0):
		outputdata[0] |= 1;
	else:
		outputdata[0] &= ~1;

if (P0V4[0] != P0V4[1]):
	if (P0V4[1] != 0):
		outputdata[0] |= 2;
	else:
		outputdata[0] &= ~2;

if (P0V5[0] != P0V5[1]):
	if (P0V5[1] != 0):
		outputdata[0] |= 4;
	else:
		outputdata[0] &= ~4;