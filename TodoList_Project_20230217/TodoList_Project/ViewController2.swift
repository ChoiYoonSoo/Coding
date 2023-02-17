//
//  ViewController2.swift
//  table&present
//
//  Created by 차경태 on 2023/02/07.
//

import UIKit

class ViewController2: UIViewController {
    
    @IBOutlet weak var inputTitle: UITextField!
    @IBOutlet weak var inputContent: UITextField!
    
    @IBOutlet weak var labelSelectedTime: UILabel!
    
    @IBOutlet weak var datePicker: UIDatePicker!
    
    
    //할일과 tableview index
    var inputTime: String!
    var interval = 0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    //Done 버튼 액션함수
    @IBAction func Done(_ sender: Any) {
        let preVC = self.presentingViewController
        guard let vc = preVC as? ViewController else { return }
        
        //이미 입력된 시간대에 입력 시 오류출력
        if vc.memoTitle[self.interval] != "" {
            let cancelAlert = UIAlertController(title: "오류", message: "이미 입력된 시간입니다.", preferredStyle: UIAlertController.Style.alert)
            let onAction = UIAlertAction(title: "확인", style: UIAlertAction.Style.default,
                                         handler: nil)//{(action: UIAlertAction) -> Void in self.presentingViewController?.dismiss(animated: true)})
            
            cancelAlert.addAction(onAction)
            
            present(cancelAlert, animated: true, completion: nil)
        }
        // 비어있는 시간대에 입력시 ViewController로 할일과 index 전달
        else {
            vc.paramTitle = self.inputTitle.text
            vc.paramContent = self.inputContent.text
            vc.paramIndex = self.interval
            
            self.presentingViewController?.dismiss(animated: true) //ViewController로 이동
        }
    }
    @IBAction func btnCancel(_ sender: UIButton) {
        self.presentingViewController?.dismiss(animated: true)
        
    }
    
    // 시간에 맞게 interval 값 설정
    @IBAction func DatePicker(_ sender: UIDatePicker) {
        let datePickerView: UIDatePicker = sender
        
        let formatter: DateFormatter = DateFormatter()
        formatter.dateFormat = "a hh:mm"
        labelSelectedTime.text = formatter.string(from: datePickerView.date)
        
        let formatterHour: DateFormatter = DateFormatter()
        formatterHour.dateFormat = "HH"
        interval = (Int(formatterHour.string(from: datePickerView.date))!-1)*2
        
        let formatterMin: DateFormatter = DateFormatter()
        formatterMin.dateFormat = "mm"
        if(formatterMin.string(from: datePickerView.date) == "30") {
            
            interval += 1
        }
        

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
