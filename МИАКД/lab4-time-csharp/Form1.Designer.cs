
namespace TimeManagerLaba
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.dateTimePickerOne = new System.Windows.Forms.DateTimePicker();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.dateTimePickerTwo = new System.Windows.Forms.DateTimePicker();
            this.buttonPeriod = new System.Windows.Forms.Button();
            this.textBox = new System.Windows.Forms.TextBox();
            this.buttonNewYearCount = new System.Windows.Forms.Button();
            this.buttonChineeseYearCount = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // dateTimePickerOne
            // 
            this.dateTimePickerOne.Location = new System.Drawing.Point(28, 92);
            this.dateTimePickerOne.Name = "dateTimePickerOne";
            this.dateTimePickerOne.Size = new System.Drawing.Size(200, 22);
            this.dateTimePickerOne.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(28, 69);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(149, 17);
            this.label1.TabIndex = 1;
            this.label1.Text = "Введите первую дату";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(280, 69);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(148, 17);
            this.label2.TabIndex = 3;
            this.label2.Text = "Введите вторую дату";
            // 
            // dateTimePickerTwo
            // 
            this.dateTimePickerTwo.Location = new System.Drawing.Point(280, 92);
            this.dateTimePickerTwo.Name = "dateTimePickerTwo";
            this.dateTimePickerTwo.Size = new System.Drawing.Size(200, 22);
            this.dateTimePickerTwo.TabIndex = 2;
            // 
            // buttonPeriod
            // 
            this.buttonPeriod.Location = new System.Drawing.Point(28, 140);
            this.buttonPeriod.Name = "buttonPeriod";
            this.buttonPeriod.Size = new System.Drawing.Size(252, 44);
            this.buttonPeriod.TabIndex = 4;
            this.buttonPeriod.Text = "Рассчитать промежуток между датами";
            this.buttonPeriod.UseVisualStyleBackColor = true;
            this.buttonPeriod.Click += new System.EventHandler(this.buttonPeriod_Click);
            // 
            // textBox
            // 
            this.textBox.Location = new System.Drawing.Point(28, 200);
            this.textBox.Name = "textBox";
            this.textBox.ReadOnly = true;
            this.textBox.Size = new System.Drawing.Size(251, 22);
            this.textBox.TabIndex = 5;
            // 
            // buttonNewYearCount
            // 
            this.buttonNewYearCount.Location = new System.Drawing.Point(303, 147);
            this.buttonNewYearCount.Name = "buttonNewYearCount";
            this.buttonNewYearCount.Size = new System.Drawing.Size(197, 31);
            this.buttonNewYearCount.TabIndex = 6;
            this.buttonNewYearCount.Text = "До Нового года осталось...";
            this.buttonNewYearCount.UseVisualStyleBackColor = true;
            this.buttonNewYearCount.Click += new System.EventHandler(this.buttonNewYearCount_Click);
            // 
            // buttonChineeseYearCount
            // 
            this.buttonChineeseYearCount.Location = new System.Drawing.Point(303, 191);
            this.buttonChineeseYearCount.Name = "buttonChineeseYearCount";
            this.buttonChineeseYearCount.Size = new System.Drawing.Size(197, 31);
            this.buttonChineeseYearCount.TabIndex = 7;
            this.buttonChineeseYearCount.Text = "Восточный календарь";
            this.buttonChineeseYearCount.UseVisualStyleBackColor = true;
            this.buttonChineeseYearCount.Click += new System.EventHandler(this.buttonChineeseYearCount_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(788, 450);
            this.Controls.Add(this.buttonChineeseYearCount);
            this.Controls.Add(this.buttonNewYearCount);
            this.Controls.Add(this.textBox);
            this.Controls.Add(this.buttonPeriod);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.dateTimePickerTwo);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dateTimePickerOne);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DateTimePicker dateTimePickerOne;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.DateTimePicker dateTimePickerTwo;
        private System.Windows.Forms.Button buttonPeriod;
        private System.Windows.Forms.TextBox textBox;
        private System.Windows.Forms.Button buttonNewYearCount;
        private System.Windows.Forms.Button buttonChineeseYearCount;
    }
}

