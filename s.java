import java.io.*;
public class CandidateCode {
 private int minHeapSize;
 private int[] minHeapArray;

  private static CandidateCode createMinHeap(int size) {
  CandidateCode minHeap = new CandidateCode();
  minHeap.minHeapSize = 0;
  minHeap.minHeapArray = new int[size];
  return minHeap;
 }
 
 private static void addMinHeapValue(CandidateCode minHeap, int val){
     ++minHeap.minHeapSize;
     int i = minHeap.minHeapSize - 1;
     while (i>0 && (val < minHeap.minHeapArray[(i - 1)/2])){
         minHeap.minHeapArray[i] = minHeap.minHeapArray[(i - 1)/2];
         i = (i - 1)/2;
     }
     minHeap.minHeapArray[i] = val;
 }
 
 private static void buildMinHeap(CandidateCode minHeap){
     int n = minHeap.minHeapSize- 1;
     int i;
     for (i = (n - 1) / 2; i >= 0; --i)
         minHeapify(minHeap, i);
 }
 
 private static CandidateCode createAndBuildMinHeap(int input1[], int size)
 {
  CandidateCode minHeap = createMinHeap(size);
     for (int i = 0; i < size; ++i)
         minHeap.minHeapArray[i] = input1[i];
     minHeap.minHeapSize = size;
     buildMinHeap(minHeap);
     return minHeap;
 }
 
 private static int fetchMinValue(CandidateCode minHeap){
     int temp = minHeap.minHeapArray[0];
     minHeap.minHeapArray[0] = minHeap.minHeapArray[minHeap.minHeapSize - 1];
     --minHeap.minHeapSize;
     minHeapify(minHeap, 0);
     return temp;
 }
 
 private static boolean minHeapSizeIsOne(CandidateCode minHeap)
 {
     return (minHeap.minHeapSize == 1);
 }

  private static void exchangeMinHeapPipe(CandidateCode minHeap,int pipe1, int pipe2)        {
  int temp = minHeap.minHeapArray[pipe1];
  minHeap.minHeapArray[pipe1] = minHeap.minHeapArray[pipe2];
  minHeap.minHeapArray[pipe2] = temp;
 }

  private static void minHeapify(CandidateCode minHeap, int index) {
  int smallest = index;
  int left = 2 * index + 1;
  int right = 2 * index + 2;

   if (left < minHeap.minHeapSize && minHeap.minHeapArray[left] < minHeap.minHeapArray[smallest])
   smallest = left;

   if (right < minHeap.minHeapSize && minHeap.minHeapArray[right] < minHeap.minHeapArray[smallest])
   smallest = right;

   if (smallest != index) {
   exchangeMinHeapPipe(minHeap,smallest,index);
   minHeapify(minHeap, smallest);
  }
 }
 
 private static int[] minCost(int input1[], int input2){
     int i = 0;
     int[] output=new int[input2-1];
     CandidateCode minHeap = createAndBuildMinHeap(input1, input2);
     while (!minHeapSizeIsOne(minHeap)){
         int min     = fetchMinValue(minHeap);
         int sec_min = fetchMinValue(minHeap);
         output[i++]= (min + sec_min);
         addMinHeapValue(minHeap, min+sec_min);
     }
     return output;
 }

  public static int[] getJoinedPipes(int input1[], int input2) {
  if (input2 == 1) {
   return new int[] { 0 };
  } else {
   return minCost(input1, input2);
  }

  }

}