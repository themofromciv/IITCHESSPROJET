"""Script de diagnostic pour tester les imports."""

print("Test 1: Import des modeles...")
try:
    print("✓ Player importe avec succes")
except Exception as e:
    print(f"✗ Erreur Player: {e}")

try:
    print("✓ Match importe avec succes")
except Exception as e:
    print(f"✗ Erreur Match: {e}")

try:
    print("✓ Round importe avec succes")
except Exception as e:
    print(f"✗ Erreur Round: {e}")

try:
    print("✓ Tournament importe avec succes")
except Exception as e:
    print(f"✗ Erreur Tournament: {e}")

print("\nTest 2: Import de la base de donnees...")
try:
    print("✓ DatabaseManager importe avec succes")
except Exception as e:
    print(f"✗ Erreur DatabaseManager: {e}")

print("\nTest 3: Import des vues...")
try:
    print("✓ MainView importe avec succes")
except Exception as e:
    print(f"✗ Erreur MainView: {e}")

try:
    print("✓ PlayerView importe avec succes")
except Exception as e:
    print(f"✗ Erreur PlayerView: {e}")

try:
    print("✓ TournamentView importe avec succes")
except Exception as e:
    print(f"✗ Erreur TournamentView: {e}")

print("\nTest 4: Import des controleurs...")
try:
    print("✓ PlayerController importe avec succes")
except Exception as e:
    print(f"✗ Erreur PlayerController: {e}")

try:
    print("✓ TournamentController importe avec succes")
except Exception as e:
    print(f"✗ Erreur TournamentController: {e}")

try:
    print("✓ MainController importe avec succes")
except Exception as e:
    print(f"✗ Erreur MainController: {e}")

print("\n" + "="*50)
print("Test termine !")
print("="*50)
