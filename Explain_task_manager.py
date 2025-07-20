# তারিখ এবং সময় নিয়ে কাজ করার জন্য datetime মডিউল ইম্পোর্ট করা হয়েছে
import datetime

# টাস্ক ম্যানেজমেন্টের মূল ক্লাস ডিফাইন করা হয়েছে
class TaskManager:
    def __init__(self):
        # টাস্ক স্টোর করার জন্য একটি খালি লিস্ট ইনিশিয়ালাইজ করা হয়েছে
        self.tasks = []
        # প্রোগ্রাম শুরু হলে আগের টাস্কগুলো লোড করা হবে
        self.load_tasks()

    # নতুন টাস্ক অ্যাড করার মেথড
    def add_task(self, description, priority="medium"):
        # টাস্ক ডিকশনারি তৈরি করা হচ্ছে
        task = {
            "id": len(self.tasks) + 1,  # ইউনিক আইডি দেওয়া হচ্ছে (বর্তমান টাস্ক সংখ্যা + 1)
            "description": description,  # টাস্কের বিবরণ
            "priority": priority,       # প্রায়োরিটি (ডিফল্ট "medium")
            "completed": False,        # নতুন টাস্ক অসম্পূর্ণ হিসেবে মার্ক করা
            "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")  # বর্তমান তারিখ/সময়
        }
        # টাস্ক লিস্টে অ্যাড করা হচ্ছে
        self.tasks.append(task)
        # কনফার্মেশন মেসেজ প্রিন্ট করা
        print(f"টাস্ক অ্যাড করা হয়েছে: {description}")
        # টাস্ক সেভ করা
        self.save_tasks()

    # সব টাস্ক দেখানোর মেথড
    def list_tasks(self):
        # যদি কোনো টাস্ক না থাকে
        if not self.tasks:
            print("\nকোনো টাস্ক খুঁজে পাওয়া যায়নি!")
            return  # মেথড থেকে বের হয়ে যাওয়া

        # টাস্ক লিস্টের হেডার প্রিন্ট করা
        print("\n=== আপনার টাস্কগুলো ===")
        # প্রতিটি টাস্কের জন্য লুপ চালানো
        for task in self.tasks:
            # টাস্ক কমপ্লিট হলে (✓), অন্যথায় (○)
            status = "✓" if task["completed"] else "○"
            # ফরম্যাট করে টাস্ক ডিটেইলস প্রিন্ট করা
            print(f"{status} [{task['id']}] {task['description']} ({task['priority']}) - {task['created']}")

    # টাস্ক কমপ্লিট মার্ক করার মেথড
    def complete_task(self, task_id):
        # সব টাস্কে লুপ চালিয়ে আইডি ম্যাচ করা
        for task in self.tasks:
            if task["id"] == task_id:
                # টাস্ক কমপ্লিট হিসেবে মার্ক করা
                task["completed"] = True
                print(f"\nটাস্ক {task_id} সম্পূর্ণ হিসেবে মার্ক করা হয়েছে!")
                # পরিবর্তন সেভ করা
                self.save_tasks()
                return  # মেথড থেকে বের হয়ে যাওয়া
        # যদি টাস্ক না পাওয়া যায়
        print("\nটাস্ক খুঁজে পাওয়া যায়নি!")

    # টাস্ক ডিলিট করার মেথড
    def delete_task(self, task_id):
        # শুধু সেই টাস্কগুলো রাখা হবে যাদের আইডি ডিলিট করতে চাওয়া আইডির সাথে মেলে না
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        print(f"\nটাস্ক {task_id} ডিলিট করা হয়েছে!")
        # পরিবর্তন সেভ করা
        self.save_tasks()

    # টাস্ক ফাইলে সেভ করার মেথড
    def save_tasks(self):
        try:
            # ফাইল রাইট মোডে খোলা
            with open("tasks.txt", "w") as file:
                # প্রতিটি টাস্ক ফাইলে লিখা
                for task in self.tasks:
                    file.write(f"{task['id']},{task['description']},{task['priority']},{task['completed']},{task['created']}\n")
        except Exception as e:
            # এরর হলে মেসেজ প্রিন্ট করা
            print(f"\nটাস্ক সেভ করতে এরর: {e}")

    # ফাইল থেকে টাস্ক লোড করার মেথড
    def load_tasks(self):
        try:
            # ফাইল রিড মোডে খোলা
            with open("tasks.txt", "r") as file:
                # ফাইলের প্রতিটি লাইন পড়া
                for line in file:
                    # কমা দিয়ে সেপারেট করা অংশগুলো আলাদা করা
                    parts = line.strip().split(",")
                    # ৫টি অংশ আছে কিনা চেক করা
                    if len(parts) == 5:
                        # ফাইল থেকে ডাটা নিয়ে টাস্ক ডিকশনারি তৈরি
                        task = {
                            "id": int(parts[0]),           # স্ট্রিংকে ইন্টিজারে কনভার্ট
                            "description": parts[1],       # টাস্ক বিবরণ
                            "priority": parts[2],          # প্রায়োরিটি
                            "completed": parts[3] == "True", # স্ট্রিংকে বুলিয়ানে কনভার্ট
                            "created": parts[4]            # তৈরি করার তারিখ
                        }
                        # টাস্ক লিস্টে অ্যাড করা
                        self.tasks.append(task)
        # ফাইল না পাওয়া গেলে নতুন শুরু করা
        except FileNotFoundError:
            print("\nপূর্বের কোনো টাস্ক পাওয়া যায়নি। নতুন করে শুরু করা হচ্ছে!")
        # অন্য কোনো এরর হলে
        except Exception as e:
            print(f"\nটাস্ক লোড করতে এরর: {e}")

# মেইন ফাংশন - প্রোগ্রাম রান করবে
def main():
    # টাস্ক ম্যানেজার অবজেক্ট তৈরি
    manager = TaskManager()
    
    # মূল প্রোগ্রাম লুপ - ইউজার এক্সিট না করা পর্যন্ত চলবে
    while True:
        # মেনু অপশন প্রিন্ট করা
        print("\n=== টাস্ক ম্যানেজার ===")
        print("1. টাস্ক অ্যাড করুন")
        print("2. টাস্কগুলো দেখুন")
        print("3. টাস্ক সম্পূর্ণ করুন")
        print("4. টাস্ক ডিলিট করুন")
        print("5. প্রোগ্রাম থেকে বের হোন")

        try:
            # ইউজারের ইনপুট নেওয়া
            choice = input("\nআপনার পছন্দ ইনপুট করুন (1-5): ")
            
            # অপশন ১: নতুন টাস্ক অ্যাড করা
            if choice == "1":
                description = input("টাস্কের বিবরণ দিন: ")
                priority = input("প্রায়োরিটি দিন (high/medium/low): ").lower()
                # প্রায়োরিটি ভ্যালিডেশন
                if priority not in ["high", "medium", "low"]:
                    priority = "medium"  # ভুল ইনপুট হলে ডিফল্ট "medium"
                manager.add_task(description, priority)
                
            # অপশন ২: সব টাস্ক দেখানো
            elif choice == "2":
                manager.list_tasks()
                
            # অপশন ৩: টাস্ক কমপ্লিট মার্ক করা
            elif choice == "3":
                manager.list_tasks()  # প্রথমে টাস্কগুলো দেখানো
                try:
                    # কমপ্লিট করতে চাওয়া টাস্কের আইডি ইনপুট
                    task_id = int(input("কমপ্লিট করতে চাওয়া টাস্কের আইডি দিন: "))
                    manager.complete_task(task_id)
                except ValueError:  # যদি নাম্বার না হয়
                    print("\nসঠিক টাস্ক আইডি দিন!")
                    
            # অপশন ৪: টাস্ক ডিলিট করা
            elif choice == "4":
                manager.list_tasks()  # প্রথমে টাস্কগুলো দেখানো
                try:
                    # ডিলিট করতে চাওয়া টাস্কের আইডি ইনপুট
                    task_id = int(input("ডিলিট করতে চাওয়া টাস্কের আইডি দিন: "))
                    manager.delete_task(task_id)
                except ValueError:  # যদি নাম্বার না হয়
                    print("\nসঠিক টাস্ক আইডি দিন!")
                    
            # অপশন ৫: প্রোগ্রাম থেকে বের হওয়া
            elif choice == "5":
                print("\nআল্লাহ হাফেজ!")
                break  # লুপ থেকে বের হওয়া
                
            # ভুল ইনপুট হ্যান্ডেল করা
            else:
                print("\nভুল পছন্দ! ১ থেকে ৫ এর মধ্যে একটি সংখ্যা দিন।")
                
        # ইউজার Ctrl+C প্রেস করলে
        except KeyboardInterrupt:
            print("\n\nআল্লাহ হাফেজ!")
            break
        # অন্য কোনো এরর হলে
        except Exception as e:
            print(f"\nএকটি এরর হয়েছে: {e}")

# প্রোগ্রাম সরাসরি রান করলে এই কোড এক্সিকিউট হবে
if __name__ == "__main__":
    main()