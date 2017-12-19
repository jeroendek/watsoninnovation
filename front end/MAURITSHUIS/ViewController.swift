//
//  ViewController.swift
//  MAURITSHUIS
//
//  Created by Rik van Leeuwen on 04/12/2017.
//  Copyright © 2017 Rik van Leeuwen. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITextFieldDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    //MARK: PROPERTIES
    @IBOutlet weak var nameLabelField: UILabel!
    @IBOutlet weak var nameTextField: UITextField!
    @IBOutlet weak var codeLabelField: UILabel!
    @IBOutlet weak var codeTextField: UITextField!
    
    @IBOutlet weak var logoImageView: UIImageView!
    
    override func viewDidAppear(_ animated: Bool) {
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    //MARK: UITextFieldDelegate
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        // Hide the keyboard.
        textField.resignFirstResponder()
        return true
    }
    
    func textFieldDidEndEditing(_ textField: UITextField) {
    }
   
    //MARK: ACTIONS
    @IBAction func `continue`(_ sender: UIButton) {
    }
    
}

