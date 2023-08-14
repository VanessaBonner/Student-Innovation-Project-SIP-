#This is the main file for my project for creating a python gui research for the awarness of researching
#Started in February 27, 2023
#Date today: March 21, 2023
#Date Today: April 1, 2023
#Date Today: April 7, 2023
#Date Today: June 7, 2023
'''************************************************** THE BEGINNING OF THE LIBRARIES **************************************************'''
#libraries
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import webbrowser
from PIL import Image, ImageTk

'''************************************************** THE ENDING OF THE LIBRARIES **************************************************'''

'''************************************************** THE BEGINNING OF THE CLASSES **************************************************'''
class App:
    def __init__(self):
        # Create the main Tkinter window
        self.root = tk.Tk()
        self.root.title("DDD, Surface, Deep, Dark Web, Research Tool")
        self.root.geometry("800x800")

        # Load the background image
        self.bg_image = Image.open("Logo.png")
        self.image_data = self.get_image_data()

        # Create a Notebook widget to hold the tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Main Menu tab
        self.main_menu_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.main_menu_frame, text="Main Menu")
        self.main_menu_frame.columnconfigure(0, weight=1)
        self.main_menu_frame.rowconfigure(0, weight=1)
        self.main_menu_label = tk.Label(self.main_menu_frame, image=self.image_data)
        self.main_menu_label.grid(row=0, column=0, sticky="new")

        # Surface Web tab
        self.surface_web_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.surface_web_frame, text="Surface Web")
        self.surface_web_text = tk.Text(self.surface_web_frame, wrap=tk.WORD, font=("Helvetica", 16, "italic"))  # Add font here
        self.surface_web_text.insert("1.8", "The Surface Web, also known as the Visible Web or Clearnet, refers to the part of the World Wide Web that is easily accessible and indexed by search engines like Google, Bing, and Yahoo. It is the portion of the internet that most people are familiar with and use regularly. Some key characteristics of the Surface Web include: \n ")
        
        # Middle of the content
        middle_text = "\n 1) Publicly Accessible Content: Websites and web pages on the Surface Web are accessible to anyone with an internet connection and a web browser. They do not require any special permissions or credentials to access.\n"
        middle_text2 = "\n 2) Search Engine Indexing: Search engines continuously crawl and index the content on the Surface Web, making it easy to find information using search queries.\n"
        middle_text3 = "\n 3) Standard URLs: Websites on the Surface Web have standard URLs (Uniform Resource Locators) that begin with 'http:// also https://'. These URLs are used to navigate and access specific pages on the web.\n"
        middle_text4 = "\n 4) Regulated and Legal Content: The content on the Surface Web is generally regulated and follows legal guidelines. Websites hosted on the Surface Web are subject to various laws and regulations, depending on the country or region they are based in. \n"
        middle_text5 = "\n 5) Common Use Cases: The Surface Web is commonly used for activities such as accessing news and information, online shopping, social media, education, research, and more. \n"
        
    

        # Insert the middle text after the beginning text
        self.surface_web_text.insert("end-2c", middle_text)

        # Insert the middile text after the beginning text
        self.surface_web_text.insert("end-1c", middle_text2)

        # Insert the middile text after the beginning text
        self.surface_web_text.insert("end-1c", middle_text3)

        # Insert the middile text after the beginning text
        self.surface_web_text.insert("end-1c", middle_text4)

        # Insert the middile text after the beginning text
        self.surface_web_text.insert("end-1c", middle_text5)

        # Insert the ending text after the beginning text
        self.surface_web_text.pack(fill='both', expand=True)


        # Deep Web tab
        self.deep_web_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.deep_web_frame, text="Deep Web")
        self.deep_web_text = tk.Text(self.deep_web_frame, wrap=tk.WORD, font=("Helvetica", 16, "italic"))  # Add font here
        self.deep_web_text.insert("1.8", "The Deep Web, sometimes called the Invisible Web or Hidden Web, is a vast portion of the internet that is not indexed by traditional search engines and is not easily accessible through standard web browsers. This part of the web contains information and resources that are not meant to be easily accessible to the general public. Unlike the Surface Web, which consists of websites and pages that are openly available, the Deep Web includes content that requires specific permissions, credentials, or specialized software to access. Here are some key characteristics of the Deep Web: \n\n")
        self.deep_web_text.pack(fill='both', expand=True)

        # Middle of the content
        middle_text = "\n\n 1) Unindexed Content: The primary distinction of the Deep Web is that its content is not indexed by popular search engines. This includes databases, private websites, academic resources, and other content that is intentionally hidden from public view. \n"
        middle_text2 = "\n 2) Restricted Access: Many areas of the Deep Web require authentication or specific access credentials to be accessed. This might involve logging in with a username and password, using encryption keys, or following other security protocols. \n"
        middle_text3 = "\n 3) Privacy and Anonymity: Due to the nature of the content found on the Deep Web, users often value their privacy and anonymity. This has led to the use of specialized software like Tor (The Onion Router) to access deep web content while maintaining anonymity.\n"
        middle_text4 = "\n 4) Diverse Content: The Deep Web encompasses a wide range of content types, including private forums, subscription-based services, confidential databases, scientific research databases, academic libraries, and more. It is also rumored to host illegal marketplaces and other illicit activities. \n"
        middle_text5 = "\n 5) Legal and Ethical Considerations: While much of the Deep Web contains legitimate and lawful content, there are also portions that engage in illegal activities, such as the sale of drugs, weapons, stolen data, and other illicit goods and services. Navigating the Deep Web involves understanding potential legal and ethical risks. \n"    
        # Insert the middle text for Deep Web
        self.deep_web_text.insert("end-2c", middle_text)

        # Insert the middle text for Deep Web
        self.deep_web_text.insert("end-1c", middle_text2)

        # Insert the middle text for Deep Web
        self.deep_web_text.insert("end-1c", middle_text3)

        # Insert the middle text for Deep Web
        self.deep_web_text.insert("end-1c", middle_text4)

        # Insert the middle text for Deep Web
        self.deep_web_text.insert("end-1c", middle_text5)


        # Dark Web tab
        self.dark_web_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.dark_web_frame, text="Dark Web")
        self.dark_web_text = tk.Text(self.dark_web_frame, wrap=tk.WORD, font=("Helvetica", 16, "italic"))  # Add font here
        self.dark_web_text.insert("1.8", "The Dark Web is a subset of the Deep Web that is intentionally hidden and inaccessible through standard web browsers. It is known for hosting a range of illegal and illicit activities, as well as providing a platform for users to communicate and exchange information with a high degree of anonymity. Here's some information about the Dark Web: \n\n")
        self.dark_web_text.pack(fill='both', expand=True)

        # Middle of the content
        middle_text = "\n\n 1)Anonymity and Privacy: The Dark Web is often accessed using specialized software, with Tor (The Onion Router) being the most well-known. Tor routes internet traffic through a series of encrypted nodes, making it extremely difficult to trace the origin of a user's connection. This provides a high level of anonymity for both users and website operators. \n"
        middle_text2 = "\n 2)Onion Routing: The term 'Onion Routing' refers to the layered encryption used by Tor to pass information between nodes. This layered approach is why Tor websites are often referred to as '.onion' sites. Each layer of encryption is peeled back as data passes through each node, like the layers of an onion, hence the name. \n"
        middle_text3 = "\n 3) Illegal Activities: The Dark Web has gained notoriety for being a haven for various illegal activities, including the sale of drugs, firearms, stolen data, counterfeit currencies, and more. Black markets, known as 'Darknet Markets,' offer a platform for such transactions, often using cryptocurrencies like Bitcoin for added anonymity.\n"
        middle_text4 = "\n 4) Hacking and Cybercrime: The Dark Web is also a hub for cybercriminals offering hacking tools, services, and stolen data, such as credit card information and personal identities. Forums and marketplaces on the Dark Web facilitate these transactions. \n"
        middle_text5 = "\n 5) Whistleblowing and Anonymity: While the Dark Web is often associated with criminal activities, it also serves as a platform for whistleblowers and activists to communicate without fear of retribution. Platforms like SecureDrop allow users to anonymously submit sensitive information to journalists and organizations. \n"

        # Insert the middle text for Dark Web
        self.dark_web_text.insert("end-2c", middle_text)
       
        # Insert the middle text for Dark Web
        self.dark_web_text.insert("end-1c", middle_text2)

        # Insert the middle text for Dark Web
        self.dark_web_text.insert("end-1c", middle_text3)

        # Insert the middle text for Dark Web
        self.dark_web_text.insert("end-1c", middle_text4)

        # Insert the middle text for Dark Web
        self.dark_web_text.insert("end-1c", middle_text5)


         # Adding a hyperlink to the Surface Web text
        hyperlink_text = "\n The Surface Web: Google, Bing, Yahoo, LinkedIn. \n"
        self.surface_web_text.tag_configure("hyperlink", foreground="blue", underline=True)
        self.surface_web_text.insert("end-1c", hyperlink_text, "hyperlink")
        self.surface_web_text.tag_bind("hyperlink", "<Button-1>", self.open_link)

        # Adding a hyperlink to the Deep Web text
        hyperlink_text2 = "\n The Deep Web: Fmovies, Omegle, Element, Odysee, Bitchute. \n"
        self.deep_web_text.tag_configure("hyperlink_text2", foreground="blue", underline=True)
        self.deep_web_text.insert("end-1c", hyperlink_text2, "hyperlink_text2")
        self.deep_web_text.tag_bind("hyperlink_text2", "<Button-1>", self.open_link2)

        # Adding a hyperlink to the Dark Web text
        hyperlink_text3 = "\n The Dark Web: Tor, Torrents, DuckDuckGo, Tor66. \n"
        self.dark_web_text.tag_configure("hyperlink_text3", foreground="blue", underline=True)
        self.dark_web_text.insert("end-1c", hyperlink_text3, "hyperlink_text3")
        self.dark_web_text.tag_bind("hyperlink_text3", "<Button-1>", self.open_link3)


    def open_link(self, event):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Surface_Web")
        webbrowser.open_new("https://www.google.com/")
        webbrowser.open_new("https://www.bing.com/")
        webbrowser.open_new("https://www.yahoo.com/")
        webbrowser.open_new("https://www.linkedin.com/")

    def open_link2(self, event):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Deep_web")
        webbrowser.open_new("https://fmovies.to/")
        webbrowser.open_new("https://www.omegle.com/")
        webbrowser.open_new("https://element.io/")
        webbrowser.open_new("https://www.guilded.gg/")
        webbrowser.open_new("https://odysee.com/")
        webbrowser.open_new("https://www.bitchute.com/")

    
    def open_link3(self, event):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Dark_web")
        webbrowser.open_new("https://www.torproject.org/")
        webbrowser.open_new("https://torrentfreak.com/top-torrent-sites/")
        webbrowser.open_new("http://tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion/")



    def get_image_data(self):
        # Convert the PIL image to Tkinter PhotoImage
        image_data = ImageTk.PhotoImage(self.bg_image)
        return image_data

    def run(self):
        # Start the main Tkinter event loop
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
'''************************************************** THE ENDING OF THE CLASSES **************************************************'''