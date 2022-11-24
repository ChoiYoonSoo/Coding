//
//  ViewController.swift
//  project
//
//  Created by CYS on 2022/11/24.
//

import UIKit

class ViewController: UIViewController,UIPickerViewDelegate, UIPickerViewDataSource {
    
    var imgArr1 = [UIImage?]()
    var imgArr2 = [UIImage?]()
    var imgFile = ["bottom_1.jpg","bottom_2.jpg","bottom_3.jpg","top_1.jpg","top_2.jpg","top_3.jpg","top_4.jpg","top_5.jpg"]
    var imgName1 = ["bottom_1.jpg","bottom_2.jpg","bottom_3.jpg"]
    var imgName2 = ["top_1.jpg","top_2.jpg","top_3.jpg","top_4.jpg","top_5.jpg"]
    
    @IBOutlet var imgView: UIImageView!
    @IBOutlet var lblLabel: UILabel!
    @IBOutlet var dataPicker2: UIPickerView!
    @IBOutlet var dataPicker1: UIPickerView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        for i in 0..<3{
            let img11 = UIImage(named: imgFile[i])
            imgArr1.append(img11)
        }
        
        for i in 3..<8{
            let img22 = UIImage(named: imgFile[i])
            imgArr2.append(img22)
        }
        
        lblLabel.text = "Selected item: "
        imgView.image = imgArr1[0]
    }
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        if(pickerView == dataPicker1){
            return imgName2.count
        }
        else{
            return imgName1.count
        }
    }
    
    func pickerView(_ pickerView: UIPickerView, viewForRow row: Int, forComponent component: Int, reusing view: UIView?) -> UIView {
        
        if(pickerView == dataPicker1){
            let img = UIImageView(image: imgArr2[row])
            img.frame = CGRect(x:0, y:0, width: 200, height:500)
            return img
        }
        else{
            let img2 = UIImageView(image: imgArr1[row])
            img2.frame = CGRect(x:0, y:0, width: 200, height: 500)
            return img2
        }
    }
    
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        if(pickerView == dataPicker1){
            lblLabel.text = "Selected item: " + imgName2[row]
        }
        else{
            imgView.image = imgArr1[row]
        }
    }
    
    
}

