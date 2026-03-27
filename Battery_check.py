# A simple Logic Engine for your gym days
gym_day = True
muscle_group = "Legs"
intensity_score = 10

print("--- Workout Analysis ---")

if gym_day and intensity_score >= 8:
    print(f"🔥 Massive session on {muscle_group}!")
    print("Action: Increase protein intake and prioritize sleep.")
elif gym_day:
    print(f"✅ Solid {muscle_group} work. Keep the momentum.")
else:
    print("💤 Rest day. Focus on mobility and hydration.")

# A simple loop to show Python's speed
print("\nCounting your reps:")
for i in range(1, 6):
    print(f"Rep {i}... PUSH!")





