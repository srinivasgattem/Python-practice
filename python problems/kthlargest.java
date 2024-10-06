import java.util.PriorityQueue;

class kthlargest{
    public int findkthlargest(int []nums,int k){
        PriorityQueue<Integer> minHeap= new PriorityQueue<>();
        for(int num:nums){
            minHeap.add(num);
            if(minHeap.size()>k){
                minHeap.poll();
            }
        }
        return minHeap.peek();
    }

}