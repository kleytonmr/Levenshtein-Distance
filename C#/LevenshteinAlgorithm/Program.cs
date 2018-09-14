using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LevenshteinAlgorithm
{
    class Program
    {
        static void Main(string[] args)
        {
            string nm1 = "notKley", nm2 = "Kleyton";

            Console.WriteLine("Levenshtein distance: {0}", LevenshteinAlgorithm.LevenshteinDistance(nm1, nm2));
            Console.WriteLine("Levenshtein distance: {0}%", LevenshteinAlgorithm.Compare(nm1, nm2));

            Console.ReadKey();
        }
    }
}
