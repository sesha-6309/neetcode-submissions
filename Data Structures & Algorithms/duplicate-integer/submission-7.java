class Solution{
    public boolean hasDuplicate(int[] nums){
      HashSet<Integer> kl = new HashSet<>();
      for(int num:nums){
        if(kl.contains(num)){
            return true;
        }
        kl.add(num);
      }
      return false;
    }}