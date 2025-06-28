import os
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")  # Force safe backend for GUI

import logging
logging.basicConfig(filename="my_weight_app.log", level=logging.CRITICAL, format="%(asctime)s - %(levelname)s - %(message)s")
import matplotlib.dates as mdates


plt.rcParams['font.family'] = 'Microsoft YaHei'

# Define file path to store weight data
DATA_FOLDER = "weight_data"
DATA_FILE = os.path.join(DATA_FOLDER, "daily_weights.csv")
ICON_ICO_PATH = "./Han_icon.ico"  # Use .ico for Windows
ICON_PNG_PATH = "./Han_icon.ico"  # Use .png for Windows
icon_img_global = None

open_charts = []

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


# Ensure data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Function to add a new weight entry
def add_weight_entry(weight):
    today = datetime.now().strftime("%y/%m/%d")
    new_entry = pd.DataFrame([[today, weight]], columns=["Date", "Weight"])

    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        df = df[df.Date != today]  # avoid duplicate entries for the same day
        df = pd.concat([df, new_entry], ignore_index=True)
    else:
        df = new_entry

    df.to_csv(DATA_FILE, index=False)
    messagebox.showinfo("成功", f"记录了{today}的体重：{weight} kg.")


# Function to plot the weight chart with matplotlib inside the GUI
def plot_weight_chart_matplotlib(window):
    if not os.path.exists(DATA_FILE):
        messagebox.showerror("错误", "无体重数据.")
        return

    df = pd.read_csv(DATA_FILE)
    df.columns = df.columns.str.strip()  # 清除列名周围的空格
    if "Date" not in df.columns or "Weight" not in df.columns:
        messagebox.showerror("CSV Format Error", "CSV file must have columns: Date,Weight")
        return

    df['Date'] = pd.to_datetime(df['Date'], format="%y/%m/%d", errors='coerce')
    df = df.sort_values('Date')
    df = df.dropna()
    df = df[df['Weight'].apply(lambda x: pd.to_numeric(x, errors='coerce')).notnull()]

    dates = df['Date']
    weights = df['Weight'].astype(float)

    # Create matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 4), dpi=120)
    line, = ax.plot(dates, weights, color='deepskyblue', linewidth=2.5, label='趋势')
    scatter = ax.scatter(dates, weights, color='black', s=50, edgecolors='white', label='记录点')

    # Set the date format for the x-axis
    date_format = mdates.DateFormatter('%y/%m/%d')
    ax.xaxis.set_major_formatter(date_format)

    ax.set_title("体重变化图", fontsize=16, fontweight='bold')
    ax.set_xlabel("日期")
    ax.set_ylabel("体重(kg)")
    ax.grid(True, linestyle='--', alpha=0.5)
    fig.autofmt_xdate()
    ax.legend()

    # Set the x-axis labels to horizontal
    plt.xticks(rotation=0)

    # Tooltip effect
    annot = ax.annotate("", xy=(0,0), xytext=(15,15), textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(ind):
        x, y = scatter.get_offsets()[ind["ind"][0]]
        annot.xy = (x, y)
        text = f"{df['Date'].iloc[ind['ind'][0]].strftime('%y/%m/%d')}: {weights.iloc[ind['ind'][0]]:.2f} kg"
        annot.set_text(text)
        annot.get_bbox_patch().set_facecolor('skyblue')
        annot.get_bbox_patch().set_alpha(0.9)
        annot.set_fontsize(10)
        annot.set_fontweight('bold')

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = scatter.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    # Embed in Tkinter window
    top = tk.Toplevel(window)
    top.withdraw()  # Hide the window while configuring
    top.title("体重图")
    # top.geometry("1400x800")  # Set initial size of chart window
    center_window(top, 1400, 800)
    top.deiconify()  # Show the window after setting position
    def set_window_icon(window):
        global icon_img_global
        try:
            if os.path.exists(ICON_ICO_PATH):
                window.iconbitmap(ICON_ICO_PATH)
            elif os.path.exists(ICON_PNG_PATH):
                icon_img = Image.open(ICON_PNG_PATH)
                icon_img_global = ImageTk.PhotoImage(icon_img)
                window.iconphoto(True, icon_img_global)
        except Exception as e:
            print("警告: 无法设置窗口图标:", e)
    set_window_icon(top)
    # def close_chart():
    #     # print("图表窗口关闭.")
    #     top.destroy()
    # top.protocol("WM_DELETE_WINDOW", close_chart)

    open_charts.append(top)  # Track this window

    canvas = FigureCanvasTkAgg(fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    top.protocol("WM_DELETE_WINDOW", top.destroy)

# GUI application
def run_gui():
    def on_record():
        weight = weight_entry.get()
        try:
            weight = float(weight.replace(',', '.').strip())
            add_weight_entry(weight)
            weight_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("无效输入", "请输入有效数字.")

    def on_show_chart():
        try:
            plot_weight_chart_matplotlib(root)
        except Exception as e:
            logging.exception("显示图表失败")
            messagebox.showerror("图表错误", "无法显示图表. 请查看日志细节my_weight_app.log.")           

    root = tk.Tk()
    root.withdraw()  # Hide the window while configuring
    root.title("体重记录-汉要硬玩")
    # Set window icon
    root.iconbitmap(ICON_ICO_PATH)

    def on_main_close():
        # Destroy all open chart windows
        for ch in open_charts[:]:
            if ch.winfo_exists():
                ch.destroy()
                open_charts.remove(ch)
        # Close matplotlib plots cleanly
        import matplotlib.pyplot as plt
        plt.close('all')
        root.destroy()
    

    # root.geometry("350x220")
    center_window(root, 350, 220) #居中
    root.deiconify()  # Show the window after setting position
    root.configure(bg='#1e1e1e')
    root.protocol("WM_DELETE_WINDOW", on_main_close)




    tk.Label(root, text="输入今日体重(kg):", fg='white', bg='#1e1e1e', font=('Arial', 11)).pack(pady=12)
    weight_entry = tk.Entry(root, justify='center', font=('Arial', 12))
    weight_entry.pack()

    tk.Button(root, text="记录体重", command=on_record, font=('Arial', 11), bg='#3c3c3c', fg='white').pack(pady=8)
    tk.Button(root, text="显示图表", command=on_show_chart, font=('Arial', 11), bg='#3c3c3c', fg='white').pack(pady=5)

    root.mainloop()

# Run the app
if __name__ == "__main__":
    run_gui()
