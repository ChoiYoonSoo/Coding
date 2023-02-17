//
//  ViewController.swift
//  TodoList_Project
//
//  Created by 차경태 on 2023/02/07.
//

import UIKit

class ViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    

    @IBOutlet weak var tableView: UITableView!
    
    var memoTitle = [String](repeating: "", count: 48)
    var memoContent = [String](repeating: "", count: 48)
    var memoTime: [String] = ["01:00","01:30","02:00","02:30","03:00","03:30","04:00","04:30","05:00","05:30","06:00","06:30","07:00","07:30","08:00","08:30","09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30","24:00"]
    var paramTitle: String?
    var paramContent: String?
    var paramIndex: Int?
    
    //VC2에서 VC로 넘어올 때마다 전달받은 데이터들 memoTitle에 입력하고 테이블뷰 갱신
    override func viewWillAppear(_ animated: Bool) {
        if let title = paramTitle, let index = paramIndex, let content = paramContent {
            memoTitle[index] = title
            memoContent[index] = content
        }
        
        
        self.tableView.reloadData()
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.

    }
    
    //tableView delegate 메서드
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return memoTime.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard var cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath) as? CustomCell else { return UITableViewCell()}
        cell.labelTitle.text = memoTitle[indexPath.row]
        cell.labelTime.text = memoTime[indexPath.row]
        return cell
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 50.0
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "mySegue" {
            if let destination = segue.destination as?
                ViewController3 {
                if let selectedIndex = self.tableView.indexPathForSelectedRow?.row {
                    destination.prepareTitle = memoTitle[selectedIndex]
                    destination.prepareTime = memoTime[selectedIndex]
                    destination.prepareContent = memoContent[selectedIndex]
                }
            }
        }
    }
    
    

    
}
class CustomCell: UITableViewCell {
   
    @IBOutlet weak var labelTitle: UILabel!
    @IBOutlet weak var labelTime: UILabel!
    
}

