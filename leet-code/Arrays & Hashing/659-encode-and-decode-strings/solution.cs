public class Solution {

    public string Encode(IList<string> strs) 
    {
        StringBuilder builder = new StringBuilder();
        foreach(var s in strs)
        {
            builder.Append(s.Length).Append("#").Append(s);
        }
        return builder.ToString();
    }

    public List<string> Decode(string s) 
    {
        List<string> res = new List<string>();
        var i = 0;
        while(i < s.Length)
        {
            var j = i;
            while(s[j] != '#')
            {
                j++;
            }
            var length = int.Parse(s.Substring(i, j - i));
            res.Add(s.Substring(j + 1, length));
            i = j + 1 + length;
        }
        return res;
   }
}
