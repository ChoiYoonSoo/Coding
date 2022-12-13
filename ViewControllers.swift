//
//  ViewController.swift
//  imageView
//
//  Created by 최윤수 on 2022/11/03.
//

import UIKit

class ViewController: UIViewController {
    
    var isZoom = false // 전구 이미지 확대 여부에 대한 변수
    var imgOn: UIImage? // 켜진 전구 이미지에 대한 UIImage 타입의 변수
    var imgOff: UIImage? // 꺼진 전구 이미지에 대한 UIImage 타입의 변수

    @IBOutlet var imgView: UIImageView!
    @IBOutlet var btnResize: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        imgOn = UIImage(named: "lamp_on.png") // 켜진 전구 이미지에 대한 UIImage 타입의 객체로 imgOn 변수 초기화
        imgOff = UIImage(named: "lamp_off.png") // 꺼진 전구 이미지에 대한 UIImage 타입의 객체로 imgOff 변수 초기화
        imgView.image = imgOn // view를 loading한 다음 image view에 보이는 초기 이미지를 켜진 전구 이미지로 설정
    }

    @IBAction func btnResizeImage(_ sender: UIButton) {
        let scale: CGFloat = 2.0
        var newWidth:CGFloat, newHeight:CGFloat
        
        if isZoom{
            newWidth = imgView.frame.width/scale
            newHeight = imgView.frame.height/scale
            btnResize.setTitle("확대",for: .normal)
        }
        else{
            newWidth = imgView.frame.width * scale
            newHeight = imgView.frame.height * scale
            btnResize.setTitle("축소",for: .normal)
        }
        
        imgView.frame.size = CGSize(width: newWidth, height: newHeight)
        isZoom = !isZoom
    }
    
    @IBAction func switchImageOnOff(_ sender: UISwitch) {
        if sender.isOn{
            imgView.image = imgOn
        } else{
            imgView.image = imgOff
        }
    }
}

