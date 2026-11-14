import edu.princeton.cs.algs4.*;

public class MergeBU
{
    private static Comparable[] aux;

    public static void sort(Comparable[] a)
    {
        int n = a.length;
        aux = new Comparable[a.length];
        for (int len = 1; len < n; len *=2)
            for (int lo = 0; lo < n-len; lo += len+len)
                merge(a, lo, lo+len-1, Math.min(lo+len+len-1, n-1));
    }

    private static void merge(Comparable[] a, int lo, int mid, int hi)
    {
        int i = lo, j = mid+1;

        for (int k = lo; k <= hi; k++)
            aux[k] = a[k];

        for (int k = lo; k <= hi; k++)
            if      (i > mid)              a[k] = aux[j++];
            else if (j > hi)               a[k] = aux[i++];
            else if (less(aux[j], aux[i])) a[k] = aux[j++];
            else                           a[k] = aux[i++];
    }

    private static boolean less(Comparable v, Comparable w)
    { return v.compareTo(w) < 0; }

    private static void exchange(Comparable[] a, int i, int j)
    { Comparable t = a[i]; a[i] = a[j]; a[j] = t; }

    private static void show(Comparable[] a)
    { // Print array on a single line
        for (int i = 0; i < a.length; i++)
            StdOut.print(a[i] + " ");
        StdOut.println();
    }

    public static boolean isSorted(Comparable[] a)
    {
        for (int i = 1; i < a.length; i++)
            if (less(a[i], a[i-1])) return false;
        return true;
    }

    public static void main(String[] args)
    { // Usage: '4 6 5 8 4 7 3 1 1' | java -cp ".;algs4.jar" MergeBU.java
        String[] a = StdIn.readAllStrings();
        sort(a);
        assert isSorted(a);
        show(a);
    }
}