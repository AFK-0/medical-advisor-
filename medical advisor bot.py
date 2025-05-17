import tkinter as tk
from tkinter import ttk, messagebox
import json
import webbrowser
import os
from datetime import datetime

class MedicalAdvisorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Advisor")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Load medical data
        self.load_medical_data()
        
        # Initialize variables
        self.current_frame = None
        self.user_symptoms = []
        self.severity_scale = 0
        
        # Start with main screen
        self.show_main_screen()
    
    def load_medical_data(self):
        # Dictionary of wellness recommendations
        self.wellness_tips = {
            "Daily Health Tips": [
                "Drink 8-10 glasses of water daily",
                "Get 7-8 hours of sleep",
                "Eat balanced meals",
                "Exercise for 30 minutes",
                "Take breaks from screen",
                "Practice good hygiene",
                "Maintain good posture",
                "Stay mentally active"
            ]
        }

        # Dictionary of emergency scenarios
        self.emergency_scenarios = [
            "Severe Chest Pain",
            "Difficulty Breathing",
            "High Fever with Seizures",
            "Severe Accident",
            "Unconsciousness"
        ]

        # Dictionary of basic diseases and symptoms
        self.scenarios = {
            "Common Cold & Flu": {
                "symptoms": [
                    "Runny Nose",
                    "Sore Throat",
                    "Fever",
                    "Body Ache",
                    "Cough"
                ],
                "medications": {
                    "Runny Nose": ["Antihistamine", "Nasal Decongestant"],
                    "Sore Throat": ["Throat Lozenges", "Pain Reliever"],
                    "Fever": ["Paracetamol", "Ibuprofen"],
                    "Body Ache": ["Pain Reliever", "Muscle Relaxant"],
                    "Cough": ["Cough Syrup", "Throat Lozenges"]
                },
                "precautions": {
                    "Runny Nose": [
                        "Use tissue paper and dispose properly",
                        "Steam inhalation",
                        "Stay hydrated",
                        "Rest well"
                    ],
                    "Sore Throat": [
                        "Gargle with warm salt water",
                        "Drink warm fluids",
                        "Avoid cold drinks",
                        "Rest voice"
                    ],
                    "Fever": [
                        "Take rest",
                        "Stay hydrated",
                        "Use light clothing",
                        "Cool compress if needed"
                    ],
                    "Body Ache": [
                        "Get adequate rest",
                        "Warm compress",
                        "Light stretching",
                        "Avoid strenuous activity"
                    ],
                    "Cough": [
                        "Stay hydrated",
                        "Use humidifier",
                        "Avoid cold air",
                        "Elevate head while sleeping"
                    ]
                }
            },
            "Digestive Issues": {
                "symptoms": [
                    "Stomach Pain",
                    "Nausea",
                    "Diarrhea",
                    "Constipation",
                    "Indigestion"
                ],
                "medications": {
                    "Stomach Pain": ["Antacid", "Pain Reliever"],
                    "Nausea": ["Anti-nausea Medicine", "ORS"],
                    "Diarrhea": ["ORS", "Anti-diarrheal"],
                    "Constipation": ["Stool Softener", "Laxative"],
                    "Indigestion": ["Antacid", "Digestive Enzyme"]
                },
                "precautions": {
                    "Stomach Pain": [
                        "Avoid spicy foods",
                        "Eat slowly",
                        "Small frequent meals",
                        "Stay hydrated"
                    ],
                    "Nausea": [
                        "Eat light foods",
                        "Avoid strong smells",
                        "Stay hydrated",
                        "Rest after meals"
                    ],
                    "Diarrhea": [
                        "Stay hydrated with ORS",
                        "Avoid dairy products",
                        "Eat bland foods",
                        "BRAT diet (Banana, Rice, Apple, Toast)"
                    ],
                    "Constipation": [
                        "Increase fiber intake",
                        "Drink more water",
                        "Regular exercise",
                        "Don't ignore nature's call"
                    ],
                    "Indigestion": [
                        "Eat slowly",
                        "Avoid lying down after meals",
                        "Avoid trigger foods",
                        "Small frequent meals"
                    ]
                }
            },
            "Headache & Migraine": {
                "symptoms": [
                    "Mild Headache",
                    "Severe Headache",
                    "Eye Strain",
                    "Neck Pain",
                    "Sensitivity to Light"
                ],
                "medications": {
                    "Mild Headache": ["Paracetamol", "Ibuprofen"],
                    "Severe Headache": ["Migraine Medicine", "Pain Reliever"],
                    "Eye Strain": ["Eye Drops", "Pain Reliever"],
                    "Neck Pain": ["Pain Reliever", "Muscle Relaxant"],
                    "Sensitivity to Light": ["Pain Reliever", "Anti-migraine"]
                },
                "precautions": {
                    "Mild Headache": [
                        "Rest in quiet room",
                        "Stay hydrated",
                        "Massage temples",
                        "Take screen breaks"
                    ],
                    "Severe Headache": [
                        "Rest in dark room",
                        "Cold/hot compress",
                        "Avoid triggers",
                        "Get fresh air"
                    ],
                    "Eye Strain": [
                        "20-20-20 rule (Every 20 min look 20ft away for 20sec)",
                        "Adjust screen brightness",
                        "Proper lighting",
                        "Regular breaks"
                    ],
                    "Neck Pain": [
                        "Gentle stretching",
                        "Good posture",
                        "Warm compress",
                        "Avoid sudden movements"
                    ],
                    "Sensitivity to Light": [
                        "Wear sunglasses",
                        "Reduce screen brightness",
                        "Use dark mode",
                        "Avoid bright lights"
                    ]
                }
            },
            "Allergies": {
                "symptoms": [
                    "Sneezing",
                    "Itchy Eyes",
                    "Skin Rash",
                    "Runny Nose",
                    "Coughing"
                ],
                "medications": {
                    "Sneezing": ["Antihistamine", "Nasal Spray"],
                    "Itchy Eyes": ["Eye Drops", "Antihistamine"],
                    "Skin Rash": ["Anti-itch Cream", "Antihistamine"],
                    "Runny Nose": ["Nasal Decongestant", "Antihistamine"],
                    "Coughing": ["Cough Syrup", "Antihistamine"]
                },
                "precautions": {
                    "Sneezing": [
                        "Avoid triggers",
                        "Use air purifier",
                        "Keep windows closed",
                        "Regular cleaning"
                    ],
                    "Itchy Eyes": [
                        "Avoid touching eyes",
                        "Use cold compress",
                        "Wear sunglasses outside",
                        "Keep area clean"
                    ],
                    "Skin Rash": [
                        "Avoid scratching",
                        "Wear loose clothing",
                        "Keep skin cool",
                        "Use mild soap"
                    ],
                    "Runny Nose": [
                        "Use tissue paper",
                        "Steam inhalation",
                        "Stay hydrated",
                        "Avoid triggers"
                    ],
                    "Coughing": [
                        "Stay hydrated",
                        "Honey and warm water",
                        "Avoid triggers",
                        "Use humidifier"
                    ]
                }
            }
        }
    
    def show_main_screen(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Welcome message
        tk.Label(
            self.current_frame,
            text="Welcome to Medical Advisor",
            font=("Helvetica", 24, "bold"),
            bg="#f0f0f0"
        ).pack(pady=20)
        
        # Options
        tk.Button(
            self.current_frame,
            text="I'm Feeling Well - Get Health Tips",
            command=self.show_wellness_tips,
            font=("Helvetica", 14),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10
        ).pack(pady=10)

        tk.Button(
            self.current_frame,
            text="I'm Not Feeling Well",
            command=self.show_scenario_selection,
            font=("Helvetica", 14),
            bg="#FF5722",
            fg="white",
            padx=20,
            pady=10
        ).pack(pady=10)

        tk.Button(
            self.current_frame,
            text="Exit",
            command=self.root.quit,
            font=("Helvetica", 14),
            bg="#9E9E9E",
            fg="white",
            padx=20,
            pady=10
        ).pack(pady=10)

    def show_wellness_tips(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        tk.Label(
            self.current_frame,
            text="Daily Health Tips",
            font=("Helvetica", 20, "bold"),
            bg="#f0f0f0"
        ).pack(pady=20)
        
        for tip in self.wellness_tips["Daily Health Tips"]:
            tk.Label(
                self.current_frame,
                text=f"• {tip}",
                font=("Helvetica", 12),
                bg="#f0f0f0",
                wraplength=600
            ).pack(pady=5, anchor="w")
        
        tk.Button(
            self.current_frame,
            text="Back to Main Menu",
            command=self.show_main_screen,
            font=("Helvetica", 12),
            bg="#2196F3",
            fg="white"
        ).pack(pady=20)

    def show_scenario_selection(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        tk.Label(
            self.current_frame,
            text="What's Wrong?",
            font=("Helvetica", 20, "bold"),
            bg="#f0f0f0"
        ).pack(pady=20)

        # Emergency scenarios
        emergency_frame = tk.LabelFrame(
            self.current_frame,
            text="Emergency Situations",
            font=("Helvetica", 14, "bold"),
            bg="#f0f0f0",
            fg="red"
        )
        emergency_frame.pack(pady=10, padx=10, fill="x")

        for scenario in self.emergency_scenarios:
            tk.Button(
                emergency_frame,
                text=scenario,
                command=lambda s=scenario: self.show_emergency_screen(),
                font=("Helvetica", 12),
                bg="red",
                fg="white"
            ).pack(pady=5, padx=10, fill="x")

        # Non-emergency scenarios
        normal_frame = tk.LabelFrame(
            self.current_frame,
            text="Other Situations",
            font=("Helvetica", 14, "bold"),
            bg="#f0f0f0"
        )
        normal_frame.pack(pady=10, padx=10, fill="x")

        for scenario in self.scenarios.keys():
            tk.Button(
                normal_frame,
                text=scenario,
                command=lambda s=scenario: self.show_symptoms(s),
                font=("Helvetica", 12),
                bg="#2196F3",
                fg="white"
            ).pack(pady=5, padx=10, fill="x")

        tk.Button(
            self.current_frame,
            text="Back to Main Menu",
            command=self.show_main_screen,
            font=("Helvetica", 12),
            bg="#9E9E9E",
            fg="white"
        ).pack(pady=20)

    def show_symptoms(self, scenario):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.current_scenario = scenario
        
        tk.Label(
            self.current_frame,
            text=f"Select your symptoms for {scenario}:",
            font=("Helvetica", 16),
            bg="#f0f0f0"
        ).pack(pady=20)
        
        # Create checkboxes for symptoms
        self.symptom_vars = {}
        for symptom in self.scenarios[scenario]["symptoms"]:
            var = tk.BooleanVar()
            self.symptom_vars[symptom] = var
            tk.Checkbutton(
                self.current_frame,
                text=symptom,
                variable=var,
                font=("Helvetica", 12),
                bg="#f0f0f0"
            ).pack(pady=5, anchor="w")
        
        tk.Button(
            self.current_frame,
            text="Next",
            command=self.show_severity_scale,
            font=("Helvetica", 12),
            bg="#2196F3",
            fg="white"
        ).pack(pady=20)

        tk.Button(
            self.current_frame,
            text="Back",
            command=self.show_scenario_selection,
            font=("Helvetica", 12),
            bg="#9E9E9E",
            fg="white"
        ).pack(pady=10)
    
    def show_severity_scale(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        tk.Label(
            self.current_frame,
            text="On a scale of 1-10, how severe is your discomfort?",
            font=("Helvetica", 16),
            bg="#f0f0f0"
        ).pack(pady=20)
        
        self.severity = tk.Scale(
            self.current_frame,
            from_=1,
            to=10,
            orient="horizontal",
            length=400,
            font=("Helvetica", 12)
        )
        self.severity.pack(pady=20)
        
        tk.Button(
            self.current_frame,
            text="Get Recommendations",
            command=self.show_recommendations,
            font=("Helvetica", 12),
            bg="#2196F3",
            fg="white"
        ).pack(pady=20)
    
    def show_recommendations(self):
        severity = self.severity.get()
        
        if severity >= 8:
            self.show_emergency_screen()
        else:
            self.show_treatment_recommendations()
    
    def show_emergency_screen(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        tk.Label(
            self.current_frame,
            text="⚠️ EMERGENCY SITUATION DETECTED ⚠️",
            font=("Helvetica", 20, "bold"),
            fg="red",
            bg="#f0f0f0"
        ).pack(pady=20)
        
        tk.Label(
            self.current_frame,
            text="Please call emergency services immediately!",
            font=("Helvetica", 16),
            bg="#f0f0f0"
        ).pack(pady=10)
        
        tk.Button(
            self.current_frame,
            text="Call Emergency (112)",
            command=lambda: webbrowser.open("tel:112"),
            font=("Helvetica", 14),
            bg="red",
            fg="white",
            padx=20,
            pady=10
        ).pack(pady=20)

        tk.Button(
            self.current_frame,
            text="Back to Main Menu",
            command=self.show_main_screen,
            font=("Helvetica", 12),
            bg="#9E9E9E",
            fg="white"
        ).pack(pady=10)
    
    def show_treatment_recommendations(self):
        if self.current_frame:
            self.current_frame.destroy()
            
        self.current_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.current_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        tk.Label(
            self.current_frame,
            text="Recommendations",
            font=("Helvetica", 20, "bold"),
            bg="#f0f0f0"
        ).pack(pady=20)
        
        # Show selected symptoms and recommendations
        selected_symptoms = [
            symptom for symptom, var in self.symptom_vars.items() 
            if var.get()
        ]
        
        canvas = tk.Canvas(self.current_frame, bg="#f0f0f0")
        scrollbar = ttk.Scrollbar(self.current_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for symptom in selected_symptoms:
            frame = tk.LabelFrame(
                scrollable_frame,
                text=symptom,
                font=("Helvetica", 12, "bold"),
                bg="#f0f0f0"
            )
            frame.pack(pady=10, padx=10, fill="x")
            
            # Medications
            tk.Label(
                frame,
                text="Recommended Medications:",
                font=("Helvetica", 11, "bold"),
                bg="#f0f0f0"
            ).pack(anchor="w")
            
            for med in self.scenarios[self.current_scenario]["medications"][symptom]:
                tk.Label(
                    frame,
                    text=f"• {med}",
                    bg="#f0f0f0"
                ).pack(anchor="w")
            
            # Precautions
            tk.Label(
                frame,
                text="\nPrecautions and Care:",
                font=("Helvetica", 11, "bold"),
                bg="#f0f0f0"
            ).pack(anchor="w")
            
            for precaution in self.scenarios[self.current_scenario]["precautions"][symptom]:
                tk.Label(
                    frame,
                    text=f"• {precaution}",
                    bg="#f0f0f0",
                    wraplength=500
                ).pack(anchor="w")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        button_frame = tk.Frame(self.current_frame, bg="#f0f0f0")
        button_frame.pack(fill="x", pady=20)

        tk.Button(
            button_frame,
            text="Back to Main Menu",
            command=self.show_main_screen,
            font=("Helvetica", 12),
            bg="#2196F3",
            fg="white"
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="Exit",
            command=self.root.quit,
            font=("Helvetica", 12),
            bg="#9E9E9E",
            fg="white"
        ).pack(side="right", padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalAdvisorApp(root)
    root.mainloop() 