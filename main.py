import customtkinter as ctk, 

window = ctk.CTk()
window.geometry("600x400+300+300")
ctk.set_default_color_theme("Theme.json")

# Angle of projection
angle_frame = ctk.CTkFrame(window, fg_color="#eee", border_width=0)
angle_frame.pack(pady=15)

angle_label = ctk.CTkLabel(angle_frame, text="Initial Angle of Projection: ")
angle_label.pack(side="left", padx=30)

angle = ctk.CTkEntry(angle_frame)
angle.pack(side="left")

# Initial Velocity
initial_velocity_frame = ctk.CTkFrame(window, fg_color="#eee", border_width=0)
initial_velocity_frame.pack(pady=15)

initial_velocity_label = ctk.CTkLabel(initial_velocity_frame, text="Initial Velocity: ")
initial_velocity_label.pack(side="left", padx=30)

initial_velocity_entry = ctk.CTkEntry(initial_velocity_frame)
initial_velocity_entry.pack(side="left")

# Starting Simulation
def startFunc():
	pass

start = ctk.CTkButton(window, text="Start Simulation", command=startFunc)
start.pack(pady=15)

window.mainloop()