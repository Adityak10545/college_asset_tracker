# Copyright (c) 2024, Aditya Kolekar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AssetTransfer(Document):
    def on_submit(self):
        # Loop through each asset in the Assets to Transfer child table
        for item in self.assets_to_transfer:
            # Fetch the corresponding Asset Master record
            asset = frappe.get_doc("Asset Master", item.asset)
            
            # Update the room in Asset Master to the new room (to_room)
            asset.room = self.to_room
            
            # Save the updated Asset Master record
            asset.save()

