import sys

def calculate_cardiac_output():
    print("\n--- ❤️ Cardiac Output Calculator ---")
    print("Formula: CO = Heart Rate x Stroke Volume")
    
    try:
        hr = float(input("Enter Heart Rate (beats/min): "))
        sv = float(input("Enter Stroke Volume (mL): "))
        
        # Calculate CO (mL/min) and convert to Liters
        co_ml = hr * sv
        co_liters = co_ml / 1000
        
        print(f"✅ Cardiac Output: {co_liters:.2f} L/min")
        
    except ValueError:
        print("Error: Please enter numbers only.")

def calculate_map():
    print("\n--- 🩸 Mean Arterial Pressure (MAP) Calculator ---")
    print("Formula: MAP = Diastolic + 1/3(Pulse Pressure)")
    
    try:
        systolic = float(input("Enter Systolic BP (mmHg): "))
        diastolic = float(input("Enter Diastolic BP (mmHg): "))
        
        # Pulse Pressure = Systolic - Diastolic
        pulse_pressure = systolic - diastolic
        map_value = diastolic + (1/3 * pulse_pressure)
        
        print(f"✅ MAP: {map_value:.2f} mmHg")
        
    except ValueError:
        print("Error: Please enter numbers only.")

def calculate_beta_oxidation():
    print("\n--- ⚡ Beta Oxidation ATP Calculator ---")
    print("Calculates ATP yield for a saturated, even-chain fatty acid.")
    
    try:
        carbons = int(input("Enter number of Carbon atoms (e.g., 16 for Palmitic): "))
        
        # Validation: Must be even and positive
        if carbons % 2 != 0:
            print("⚠️ This tool currently supports EVEN carbon chains only.")
            return
        
        # The Calculations
        acetyl_coa = carbons // 2
        rounds = acetyl_coa - 1
        
        # ATP Breakdown (Modern P/O Ratios: NADH=2.5, FADH2=1.5 -> 4 ATP per round)
        # Acetyl-CoA = 10 ATP (via Krebs)
        atp_from_rounds = rounds * 4
        atp_from_krebs = acetyl_coa * 10
        activation_cost = 2
        
        total_atp = atp_from_rounds + atp_from_krebs - activation_cost
        
        # Display Results
        print(f"\n🧪 Breakdown for {carbons}-Carbon Fatty Acid:")
        print(f"   • {rounds} Rounds of Beta Oxidation")
        print(f"   • {acetyl_coa} Acetyl-CoA produced")
        print(f"   • Total Net Yield: {total_atp} ATP")
        
    except ValueError:
        print("Error: Please enter a whole number.")

def main():
    while True:
        print("\n=== 🧬 Student Physiology Toolkit ===")
        print("1. Calculate Cardiac Output")
        print("2. Calculate Mean Arterial Pressure (MAP)")
        print("3. Calculate Beta Oxidation ATP")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            calculate_cardiac_output()
        elif choice == '2':
            calculate_map()
        elif choice == '3':
            calculate_beta_oxidation()
        elif choice == '4':
            print("Goodbye! Study hard.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
