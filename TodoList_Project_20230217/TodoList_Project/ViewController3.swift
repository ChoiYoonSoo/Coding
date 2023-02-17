//
//  ViewController3.swift
//  TodoList_Project
//
//  Created by 차경태 on 2023/02/10.
//

import UIKit

class ViewController3: UIViewController {
    var prepareTitle = ""
    var prepareContent = ""
    var prepareTime = ""
    
    
    @IBOutlet weak var timeLable: UILabel!
    
    @IBOutlet weak var titleText: UITextField!
    
    @IBOutlet weak var contentText: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        timeLable.text = prepareTime
        titleText.text = prepareTitle
        contentText.text = prepareContent
    }
    
    
    @IBAction func btnDone(_ sender: UIButton) {
        let preVC = self.presentingViewController
        guard let vc = preVC as? ViewController else { return }
        
            vc.paramTitle = titleText.text
            vc.paramContent = contentText.text
   
        
        
        self.presentingViewController?.dismiss(animated: true)
        
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */
    
}
