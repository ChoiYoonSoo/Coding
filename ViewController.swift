//
//  ViewController.swift
//  DatePicker
//
//  Created by 최윤수 on 2022/11/10.
//

import UIKit

class ViewController: UIViewController {
    
    let interval = 1.0
    var count = 0
    
    @IBOutlet var lblCurrentTime: UILabel!
    @IBOutlet var lblPrickerTime: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        Timer.scheduledTimer(timeInterval: interval, target: self, selector: #selector(self.updateTime), userInfo: nil, repeats: true)
    }

    @IBAction func changeDatePicker(_ sender: UIDatePicker) {
        let datePickerView: UIDatePicker = sender
        
        let formatter: DateFormatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd HH:mm EEEE"
        lblPrickerTime.text = "선택시간: " + formatter.string(from: datePickerView.date)
    }
    
    @objc func updateTime(){
        let date = Date()
        let formatter = DateFormatter(); // 현재 날짜를 얻어옴
        
        formatter.dateFormat = "yyyy-MM-dd HH:mm:ss EEEE" // 현재 날짜 포맷 설정
        
        // 현재 날짜와 함수 실행 경과 시간(초)을 레이블 lblCurrentTime의 텍스트에 표시
        lblCurrentTime.text = "현재시간: " + formatter.string(from: date) + "\n경과시간(초): " + String(self.count)
        
        self.count = self.count + 1
    }
    
}

