import re

def extract_ips_from_log(log_file_path, output_file_path):
    """
    Extract unique IP addresses from a log file and save to output file
    """
    # Regular expression pattern for IP addresses
    # Matches: 192.168.1.1, 10.0.0.1, etc.
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    
    # Set to store unique IP addresses (automatically removes duplicates)
    unique_ips = set()
    
    try:
        # Open and read the log file
        with open(log_file_path, 'r') as log_file:
            print(f"Reading log file: {log_file_path}")
            
            # Read file line by line
            for line_number, line in enumerate(log_file, 1):
                # Find all IP addresses in this line
                ips_found = re.findall(ip_pattern, line)
                
                # Add each IP to our set (duplicates automatically ignored)
                for ip in ips_found:
                    unique_ips.add(ip)
                    
            print(f"Processed {line_number} lines")
            print(f"Found {len(unique_ips)} unique IP addresses")
    
    except FileNotFoundError:
        print(f"Error: Log file '{log_file_path}' not found!")
        return
    except Exception as e:
        print(f"Error reading log file: {e}")
        return
    
    # Save unique IPs to output file
    try:
        with open(output_file_path, 'w') as output_file:
            # Convert set to sorted list for better readability
            sorted_ips = sorted(unique_ips, key=lambda x: [int(i) for i in x.split('.')])
            
            for ip in sorted_ips:
                output_file.write(ip + '\n')
                
        print(f"Unique IP addresses saved to: {output_file_path}")
        
    except Exception as e:
        print(f"Error writing to output file: {e}")

# Example usage
if __name__ == "__main__":
    # You can change these file paths
    log_file = "access.log"  # Input log file
    output_file = "ips.txt"  # Output file
    
    extract_ips_from_log(log_file, output_file)
    
    # Print first few IPs as preview
    try:
        with open(output_file, 'r') as f:
            ips = f.read().strip().split('\n')
            print(f"\nPreview of extracted IPs:")
            for ip in ips[:10]:  # Show first 10
                print(f"  {ip}")
            if len(ips) > 10:
                print(f"  ... and {len(ips) - 10} more")
    except:
        pass