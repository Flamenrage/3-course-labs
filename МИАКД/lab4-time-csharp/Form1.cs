using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TimeManagerLaba
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


        private void buttonPeriod_Click(object sender, EventArgs e)
        {
            TimeSpan difference = getDateDifference(dateTimePickerTwo.Value, dateTimePickerOne.Value);

            //Now you can do what you want with the TimeSpan.

            int differenceInDays = difference.Days;
            int differenceInHours = difference.Hours;

            textBox.Text = differenceInDays.ToString() + " дн. ";
        }

        TimeSpan getDateDifference(DateTime date1, DateTime date2)
        {
            TimeSpan ts = date1 - date2;

            return ts;
        }

        private void buttonNewYearCount_Click(object sender, EventArgs e)
        {
            DateTime nextYear = new DateTime(DateTime.Now.Year + 1, 1, 1);
            TimeSpan ts = nextYear - DateTime.Now;
            textBox.Text = string.Format("До Нового Года осталось {0} дн, {1} часов, {2} минут, {3} секунд",
                ts.Days, ts.Hours, ts.Minutes, ts.Seconds);
        }

        private void buttonChineeseYearCount_Click(object sender, EventArgs e)
        {
            int factor = 0, year, anim = 0;
            Dictionary<int, string> colors = new Dictionary<int, string> { { 1, "синего" }, { 2, "красного" }, { 3, "желтого" }, { 4, "белого" }, { 5, "черного" }, { 11, "синего" }, { 12, "красного" }, { 13, "желтого" }, { 14, "белого" }, { 15, "черного" }, };
            Dictionary<int, string> animals = new Dictionary<int, string> { { 1, "мыши" }, { 2, "быка" }, { 3, "тигра" }, { 4, "зайца" }, { 5, "дракона" }, { 6, "змеи" }, { 7, "лошади" }, { 8, "овцы" }, { 9, "обезьяны" }, { 10, "петуха" }, { 11, "собаки" }, { 12, "свиньи" }, };
            year = Convert.ToInt32(DateTime.Now.Year);
            for (int i = 1864; i <= year; i += 2)
            {
                factor++;
                if (factor >= 6)
                    factor = 1;
            }
            for (int i = 1864; i <= year; i++)
            {
                anim++;
                if (anim >= 13)
                    anim = 1;
            }
            if (anim == 2 || anim == 3 || anim == 4 || anim == 5 || anim == 10)
                factor += 10;

            textBox.Text = "Год " +  animals[anim] + " " + colors[factor] + " цвета ";
        }
    }
}
