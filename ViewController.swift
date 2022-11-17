//
//  ViewController.swift
//  PickerView
//
//  Created by CYS on 2022/11/17.
//

import UIKit

class ViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource {

    let MAX_ARRAY_NUM = 10 // 배열 imageFileName의 크기
    let PICKER_VIEW_COLUMN = 3 // Picker View의 component (column)의 수
    let PICKER_VIEW_HEIGHT: CGFloat = 80.0 // Picker View의 row의 높이
    var imageArray = [UIImage?]() // Image View에서 보여줄 이미지들로 구성된 배열
    var imageFileName = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg","9.jpg","10.jpg"] // Picker View에서 보여줄 이미지 파일명
    
    @IBOutlet var lblImageFileName: UILabel!
    @IBOutlet var pickerImage: UIPickerView!
    @IBOutlet var imageView: UIImageView!
    @IBOutlet var imageView2: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        for i in 0..<MAX_ARRAY_NUM{
            let image = UIImage(named: imageFileName[i])
            imageArray.append(image)
        }
        
        lblImageFileName.text = imageFileName[0]
        imageView.image = imageArray[0]
        imageView2.image = imageArray[0]
    }
    
    // Picker View에서 표시되는 component (column)의 수를 Picker View에게 전달하는 델리게이트 메서드
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return PICKER_VIEW_COLUMN
    }

    // Picker View에서 표시되는 component (column)내의 row 수를 Picker View에게 전달하는 델리게이트 메서드
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return imageFileName.count
    }
    
    // Picker View에서 표시되는 component (column) 내의 각 row의 title을 Picker View에게 전달하는 델리게이트 메서드
    //func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
    //    return imageFileName[row]
    //}
    
    // Picker View에서 선택한 이미지 이름을 레이블 lblImageFileName과 이미지 뷰 imageView에 표시하는 델리게이트 메서드
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        if(component == 0){ // 첫 번째 항목은 레이블의 제목을 변경
            lblImageFileName.text = imageFileName[row]
        } else if component == 1 { // 두 번째 항목은 이미지 뷰를 변경
            imageView.image = imageArray[row]
        } else if component == 2 {
            imageView2.image = imageArray[row]
        }
        
        //lblImageFileName.text = imageFileName[row]
        //imageView.image = imageArray[row]
    }
    
    // Picker View에 표시되는 componenet (column) 내의 각 row의 image를 Picker View에게 전달하는 델리게이트 메서드
    func pickerView(_ pickerView: UIPickerView, viewForRow row: Int, forComponent component: Int, reusing view: UIView?) -> UIView {
        let imgView = UIImageView(image: imageArray[row])
        imgView.frame = CGRect(x:0, y: 0, width: 100, height: 150) // Image View의 프레임 크기 섫정
        
        return imgView
    }
    
    func pickerView(_ pickerView: UIPickerView, rowHeightForComponent component: Int) -> CGFloat {
        return PICKER_VIEW_HEIGHT
    }
    
    
}

