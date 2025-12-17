# Filename: src/L2/MP2/contact_manager.py

"""
📱 Contact Manager - Level 2 Mini Project 2

A complete contact management application demonstrating:
- File I/O (reading/writing text files)
- Functions (well-organized, documented code)
- Error handling (graceful handling of errors)
- Sets (unique tags for contacts)
- List comprehensions (searching and filtering)

Author: Python Learner
Level: 2 - Nerd → Novice
"""

import os

# ============================================================
# CONSTANTS
# ============================================================
CONTACTS_FILE = "contacts.txt"
SEPARATOR = "|"


# ============================================================
# FILE OPERATIONS
# ============================================================

def load_contacts(filename):
    """
    Load contacts from a text file.
    
    File format: name|phone|email|tag1,tag2,tag3
    
    Args:
        filename: Path to the contacts file
        
    Returns:
        List of contact dictionaries
    """
    contacts = []
    
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                # Parse the line
                parts = line.split(SEPARATOR)
                if len(parts) >= 2:
                    contact = {
                        "name": parts[0],
                        "phone": parts[1],
                        "email": parts[2] if len(parts) > 2 else "",
                        "tags": set(parts[3].split(",")) if len(parts) > 3 and parts[3] else set()
                    }
                    contacts.append(contact)
                    
    except FileNotFoundError:
        print("📁 No existing contacts file found. Starting fresh!")
    except Exception as e:
        print(f"❌ Error loading contacts: {e}")
        
    return contacts


def save_contacts(filename, contacts):
    """
    Save contacts to a text file.
    
    Args:
        filename: Path to save the contacts
        contacts: List of contact dictionaries
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filename, "w") as file:
            for contact in contacts:
                # Convert tags set to comma-separated string
                tags_str = ",".join(sorted(contact["tags"])) if contact["tags"] else ""
                
                # Build the line
                line = f"{contact['name']}{SEPARATOR}{contact['phone']}{SEPARATOR}{contact['email']}{SEPARATOR}{tags_str}\n"
                file.write(line)
                
        print(f"💾 Saved {len(contacts)} contact(s) to {filename}")
        return True
        
    except IOError as e:
        print(f"❌ Error saving contacts: {e}")
        return False


# ============================================================
# CONTACT MANAGEMENT
# ============================================================

def add_contact(contacts):
    """
    Add a new contact interactively.
    
    Args:
        contacts: Current list of contacts
        
    Returns:
        Updated list with new contact (or unchanged if cancelled)
    """
    print("\n" + "=" * 40)
    print("➕ ADD NEW CONTACT")
    print("=" * 40)
    
    # Get required fields with validation
    name = input("Name (required): ").strip()
    if not name:
        print("❌ Name is required! Contact not added.")
        return contacts
    
    # Check for duplicate name
    existing_names = [c["name"].lower() for c in contacts]
    if name.lower() in existing_names:
        print(f"❌ A contact named '{name}' already exists!")
        return contacts
    
    phone = input("Phone (required): ").strip()
    if not phone:
        print("❌ Phone is required! Contact not added.")
        return contacts
    
    # Get optional fields
    email = input("Email (optional, press Enter to skip): ").strip()
    
    tags_input = input("Tags (comma-separated, e.g., work,friend): ").strip()
    # Use set comprehension to create unique, cleaned tags
    tags = {tag.strip().lower() for tag in tags_input.split(",") if tag.strip()}
    
    # Create and add the new contact
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "tags": tags
    }
    
    contacts.append(new_contact)
    print(f"\n✅ Contact '{name}' added successfully!")
    
    return contacts


def search_contacts(contacts, query):
    """
    Search contacts by name, phone, or email using list comprehension.
    
    Args:
        contacts: List of contacts to search
        query: Search string (case-insensitive)
        
    Returns:
        List of matching contacts
    """
    query_lower = query.lower()
    
    # List comprehension with multiple conditions
    matches = [
        contact for contact in contacts
        if query_lower in contact["name"].lower()
        or query_lower in contact["phone"]
        or query_lower in contact["email"].lower()
    ]
    
    return matches


def delete_contact(contacts, name):
    """
    Delete a contact by name.
    
    Args:
        contacts: Current list of contacts
        name: Name of contact to delete
        
    Returns:
        Updated list with contact removed
    """
    name_lower = name.lower()
    original_count = len(contacts)
    
    # Use list comprehension to filter out the contact
    contacts = [c for c in contacts if c["name"].lower() != name_lower]
    
    if len(contacts) < original_count:
        print(f"✅ Contact '{name}' deleted successfully!")
    else:
        print(f"❌ No contact named '{name}' found.")
    
    return contacts


def get_contacts_by_tag(contacts, tag):
    """
    Filter contacts by tag using list comprehension with set membership.
    
    Args:
        contacts: List of all contacts
        tag: Tag to filter by
        
    Returns:
        List of contacts with the specified tag
    """
    tag_lower = tag.lower()
    return [c for c in contacts if tag_lower in c["tags"]]


def get_all_tags(contacts):
    """
    Get all unique tags from all contacts.
    
    Uses set union to combine all tags.
    
    Args:
        contacts: List of all contacts
        
    Returns:
        Set of all unique tags
    """
    all_tags = set()
    for contact in contacts:
        all_tags = all_tags.union(contact["tags"])
    return all_tags


# ============================================================
# DISPLAY FUNCTIONS
# ============================================================

def display_contact(contact, number=None):
    """
    Display a single contact in a formatted way.
    
    Args:
        contact: Contact dictionary to display
        number: Optional number to display (for lists)
    """
    prefix = f"{number}. " if number else "   "
    
    print(f"\n{prefix}📇 {contact['name']}")
    print(f"      📞 Phone: {contact['phone']}")
    
    if contact['email']:
        print(f"      📧 Email: {contact['email']}")
    
    if contact['tags']:
        tags_display = ", ".join(sorted(contact['tags']))
        print(f"      🏷️  Tags: {tags_display}")


def display_all_contacts(contacts):
    """Display all contacts in a numbered list."""
    if not contacts:
        print("\n📭 No contacts found. Add some contacts first!")
        return
    
    print("\n" + "=" * 50)
    print(f"📋 ALL CONTACTS ({len(contacts)} total)")
    print("=" * 50)
    
    for i, contact in enumerate(contacts, 1):
        display_contact(contact, number=i)
    
    print("\n" + "-" * 50)


def display_statistics(contacts):
    """Display contact statistics."""
    print("\n" + "=" * 40)
    print("📊 CONTACT STATISTICS")
    print("=" * 40)
    
    print(f"   📇 Total contacts: {len(contacts)}")
    
    # Count contacts with email
    with_email = len([c for c in contacts if c["email"]])
    print(f"   📧 With email: {with_email}")
    
    # Get all tags
    all_tags = get_all_tags(contacts)
    print(f"   🏷️  Unique tags: {len(all_tags)}")
    
    if all_tags:
        print(f"      Tags: {', '.join(sorted(all_tags))}")
    
    print("-" * 40)


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("📱 CONTACT MANAGER")
    print("=" * 50)
    print("   1. 📋 View all contacts")
    print("   2. ➕ Add new contact")
    print("   3. 🔍 Search contacts")
    print("   4. 🏷️  View contacts by tag")
    print("   5. 🗑️  Delete contact")
    print("   6. 📊 View statistics")
    print("   0. 💾 Save and Exit")
    print("=" * 50)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    """
    Main entry point of the Contact Manager application.
    
    Implements the main menu loop and handles user interaction.
    """
    print("\n" + "🚀" * 25)
    print("\n   Welcome to CONTACT MANAGER!")
    print("   Level 2 Mini Project 2")
    print("\n" + "🚀" * 25)
    
    # Load existing contacts
    contacts = load_contacts(CONTACTS_FILE)
    print(f"\n📂 Loaded {len(contacts)} contact(s)")
    
    # Track if changes were made
    changes_made = False
    
    while True:
        show_menu()
        
        try:
            choice = input("\nEnter your choice (0-6): ").strip()
            
            if choice == "1":
                # View all contacts
                display_all_contacts(contacts)
                
            elif choice == "2":
                # Add new contact
                original_count = len(contacts)
                contacts = add_contact(contacts)
                if len(contacts) > original_count:
                    changes_made = True
                    
            elif choice == "3":
                # Search contacts
                query = input("\n🔍 Enter search term: ").strip()
                if query:
                    results = search_contacts(contacts, query)
                    if results:
                        print(f"\n✅ Found {len(results)} match(es):")
                        for contact in results:
                            display_contact(contact)
                    else:
                        print(f"\n❌ No contacts matching '{query}' found.")
                else:
                    print("❌ Please enter a search term.")
                    
            elif choice == "4":
                # View by tag
                all_tags = get_all_tags(contacts)
                if all_tags:
                    print(f"\n🏷️  Available tags: {', '.join(sorted(all_tags))}")
                    tag = input("Enter tag to filter by: ").strip()
                    if tag:
                        tagged = get_contacts_by_tag(contacts, tag)
                        if tagged:
                            print(f"\n✅ Contacts with tag '{tag}':")
                            for contact in tagged:
                                display_contact(contact)
                        else:
                            print(f"\n❌ No contacts with tag '{tag}'")
                else:
                    print("\n📭 No tags found. Add tags when creating contacts!")
                    
            elif choice == "5":
                # Delete contact
                if contacts:
                    display_all_contacts(contacts)
                    name = input("\n🗑️  Enter name to delete: ").strip()
                    if name:
                        original_count = len(contacts)
                        contacts = delete_contact(contacts, name)
                        if len(contacts) < original_count:
                            changes_made = True
                else:
                    print("\n📭 No contacts to delete!")
                    
            elif choice == "6":
                # View statistics
                display_statistics(contacts)
                
            elif choice == "0":
                # Save and exit
                if changes_made:
                    save_contacts(CONTACTS_FILE, contacts)
                else:
                    print("📝 No changes to save.")
                    
                print("\n👋 Thank you for using Contact Manager!")
                print("   Goodbye! 👋\n")
                break
                
            else:
                print("\n❌ Invalid choice. Please enter a number from 0 to 6.")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Operation cancelled.")
            save_choice = input("Save before exit? (y/n): ").strip().lower()
            if save_choice == 'y':
                save_contacts(CONTACTS_FILE, contacts)
            print("👋 Goodbye!")
            break
            
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
            print("   Please try again.")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
