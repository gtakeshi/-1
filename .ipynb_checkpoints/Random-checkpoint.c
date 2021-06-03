#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double urand(){   //[-1,1]の一様分布を生成		
    double m, n;
    m = RAND_MAX + 1;
    n = (rand() + 0.5)/m;
    n = (rand() + n)/m;
    return (-2)*((rand() + n)/m)-1;
}

	
int main(){  //ここでマルサグリア法を用いて､球中平面の点を探す
	double a[1000],b[1000];     //球中平面の点の座標を格納場所
	double x[1000],y[1000],z[1000];  //球面一様分布の点の座標
    int i = 0;
    srand((unsigned int)time(NULL));   //ランダムの種を時間に設定			
    while(i<1000){   //1000個の球中平面の点を生成
        double v = urand();     
        double t = urand();
        if((pow(v,2) + pow(t,2)) < 1){  	
        	//printf("%f,%f\n",v,t);
        	a[i] = v;
        	b[i] = t;
        	i++;
        }
    }
    printf("***X軸*******Y軸********Z軸***\n");
    for (int i = 0; i < 1000; i++){
     	double PowR = pow(a[i],2) + pow(b[i],2); //球の計算式で半径の平方を求める
		x[i] = 2*a[i]*sqrt(1-PowR);   
		y[i] = 2*b[i]*sqrt(1-PowR);
		z[i] = 1-2*PowR;
		printf("%f,%f,%f\n",x[i],y[i],z[i]);
     } //球面一様分布の点の座標を生成する
    return 0;
}