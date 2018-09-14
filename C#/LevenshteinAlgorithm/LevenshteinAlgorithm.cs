﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace LevenshteinAlgorithm
{
    public static class LevenshteinAlgorithm
    {


        public static int LevenshteinDistance(string source, string target)
        {
            if (String.IsNullOrEmpty(source))
            {
                if (String.IsNullOrEmpty(target)) return 0;
                return target.Length;
            }
            if (String.IsNullOrEmpty(target)) return source.Length;

            if (source.Length > target.Length)
            {
                var temp = target;
                target = source;
                source = temp;
            }

            var m = target.Length;
            var n = source.Length;
            var distance = new int[2, m + 1];

            for (var j = 1; j <= m; j++) distance[0, j] = j;

            var currentRow = 0;
            for (var i = 1; i <= n; ++i)
            {
                currentRow = i & 1;
                distance[currentRow, 0] = i;
                var previousRow = currentRow ^ 1;
                for (var j = 1; j <= m; j++)
                {
                    var cost = (target[j - 1] == source[i - 1] ? 0 : 1);
                    distance[currentRow, j] = Math.Min(Math.Min(
                                distance[previousRow, j] + 1,
                                distance[currentRow, j - 1] + 1),
                                distance[previousRow, j - 1] + cost);
                }
            }
            return distance[currentRow, m];
        }

        /// <summary>
        /// Compara duas strings
        /// </summary>
        /// <param name="a">Primeira string</param>
        /// <param name="b">Segunda string</param>
        /// <returns>Retorna um valor de 0 à 255. Quanto mais alto este valor mais parecidas são as strings</returns>

        public static byte Compare(string a, string b)
        {
            double distance = LevenshteinDistance(a, b);
            if (distance == 0) return 100;
            double length = Math.Max(a.Length, b.Length);
            if (distance == length) return 0;

            double inverted = Invert(distance, length);
            byte percent = (byte)((inverted / length) * 100);
            return percent;
        }

        private static double Invert(double min, double max)
        {
            return max - min;
        }

    }
}