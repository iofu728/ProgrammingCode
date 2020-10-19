/*
 * @Author: gunjianpan
 * @Date:   2020-09-14 00:19:59
 * @Last Modified by:   gunjianpan
 * @Last Modified time: 2020-09-14 09:15:07
 */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int x = in.nextInt(); 
        double t = in.nextDouble();           
        double[] v = new double[n+1];
        for(int i = 1; i < n+1; i++){
            v[i] = in.nextInt() * 1.0/ t;         
        }
        double[][]  temp = new double[n+1][n+1];
        double[][] ma = new double[n+1][n+1];
        // Arrays.fill(temp,Double.MAX_VALUE); 
        // Arrays.fill(ma,Double.MAX_VALUE);

        for(int i = 0;i <n+1;i++){
            Arrays.fill(temp[i],Double.MAX_VALUE); 
            Arrays.fill(ma[i],Double.MAX_VALUE); 
        }
        for (int i = 0;i < n - 1;i++){
            for(int j = i + 1;j <n; j++){
                temp[i][j] = in.nextInt();
            }
        }
        for (int i = 0;i < n - 1;i++){
            for(int j = i + 1;j <n; j++){
                ma[i][j] = in.nextInt() * 1.0 / t + temp[i][j];
            }
        }

        double[][] dp = new double[n+1][n+1];
        for(int j = 1; j < n;j++){ //j是一列对角线 1-3
            for(int i = 1; i < n-j+1;i++){
                dp[i][i+j] = Math.min(ma[i][i+j],v[i+j]);//直接两点间距离，和v[j]
                System.out.println(i +" "+ (i+j)+ " "+ dp[i][i+j]);
                for(int k = 1; k < j;k++){
                    dp[i][i+j] = Math.min(Math.min(dp[i][i+k]+dp[i+k][i+j],v[i+j]), dp[i][i+j]);
                    System.out.println(i +" "+ (i+j)+ " "+k+" "+ dp[i][i+j]);

                }
            }
        }
        
    }
    
}

