//
//  ViewController3.swift
//  MAURITSHUIS
//
//  Created by Rik van Leeuwen on 10/12/2017.
//  Copyright © 2017 Rik van Leeuwen. All rights reserved.
//

import UIKit

class ViewController3: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        let jeremyGif = UIImage.gifImageWithName("ajax-loading")
        let imageView = UIImageView(image: jeremyGif)
        imageView.frame = CGRect(x: 150, y: 300, width: 65, height: 65)
        view.addSubview(imageView)
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
