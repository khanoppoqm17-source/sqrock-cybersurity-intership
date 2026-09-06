import platform
import socket
import datetime
import os

def usb_payload_sim(output_file="recon_log.txt"):
    info = {
        "timestamp": str(datetime.datetime.now()),
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "version": platform.version(),
        "user": os.getenv("USERNAME") or os.getenv("USER"),
        "cwd": os.getcwd(),
    }
    
    with open(output_file, "w") as f:
        for k, v in info.items():
            f.write(f"{k}: {v}\n")
    
    print(f"[SIM] Recon data saved to {output_file}")
    print("\n--- Collected Info ---")
    for k, v in info.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    print("\n=== USB Drop Attack Simulation (Benign) ===\n")
    usb_payload_sim()