//
//  ViewController.swift
//  Alert Practice
//
//  Created by CYS on 2022/11/26.
//

import UIKit

class ViewController: UIViewController {
    
    var img1 = UIImage(named: "lamp_on.png")
    var img2 = UIImage(named: "lamp_off.png")
    var img3 = UIImage(named: "lamp-remove.png")
    
    var lamp1 = true
    var lamp2 = true
    
    @IBOutlet var imgView1: UIImageView!
    @IBOutlet var imgView2: UIImageView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        imgView1.image = img1
        imgView2.image = img1
    }
    
    
    @IBAction func btnOn(_ sender: Any) {
        let btn = UIAlertController(title: "선택", message: "버튼을 선택하세요", preferredStyle: UIAlertController.Style.alert)
        
        let btnAction1 = UIAlertAction(title: "전구1", style: UIAlertAction.Style.default, handler:{(action) in
            if(self.lamp1 == true){
                let me = UIAlertController(title: "경고", message: "이미 전구가 켜져있습니다.", preferredStyle: UIAlertController.Style.alert)
                let ac = UIAlertAction(title: "확인", style: UIAlertAction.Style.default, handler: nil)
                
                me.addAction(ac)
                
                self.present(me, animated: true, completion: nil)
            }
            else{
                self.imgView1.image = self.img1
                self.lamp1 = true
            }
        } )
        
        let btnAction2 = UIAlertAction(title: "전구2", style:UIAlertAction.Style.default, handler:{(action) in
            if(self.lamp2==true){
                let me = UIAlertController(title: "경고", message: "이미 전구가 켜져있습니다.", preferredStyle: UIAlertController.Style.alert)
                
                let ac = UIAlertAction(title: "확인", style: UIAlertAction.Style.default, handler: nil)
                me.addAction(ac)
                
                self.present(me, animated: true, completion: nil)
            }
            else{
                self.imgView2.image = self.img1
                self.lamp2 = true
            }
            
        }
        )
        btn.addAction(btnAction1)
        btn.addAction(btnAction2)
        present(btn, animated: true, completion: nil)
        
        
    }
    
    
    @IBAction func btnOff(_ sender: Any) {
        let btn = UIAlertController(title: "선택", message: "버튼을 선택하세요.", preferredStyle: UIAlertController.Style.alert)
        
        let btnAction1 = UIAlertAction(title: "전구1", style: UIAlertAction.Style.default,
                                       handler: {(_) in
            if(self.lamp1 == true){
                let me = UIAlertController(title: "경고", message: "전구를 끌 것입니까?", preferredStyle: UIAlertController.Style.alert)
                let ac = UIAlertAction(title: "네", style: UIAlertAction.Style.default, handler: {(_) in
                    self.imgView1.image = self.img2
                    self.lamp1 = false
                    
                })
                
                let ac2 = UIAlertAction(title: "아니오", style: UIAlertAction.Style.default, handler: nil)
                
                me.addAction(ac)
                me.addAction(ac2)
                
                self.present(me, animated: true, completion: nil)
            }
            
        })
        
        let btnAction2 = UIAlertAction(title: "전구2", style:UIAlertAction.Style.default, handler: {(_) in
            if(self.lamp2 == true){
                let me = UIAlertController(title: "경고", message: "전구를 끌 것입니까?", preferredStyle: UIAlertController.Style.alert)
                
                let ac = UIAlertAction(title: "네", style: UIAlertAction.Style.default, handler: {(_) in
                    self.imgView2.image = self.img2
                    self.lamp2 = false
                    
                })
                let ac2 = UIAlertAction(title: "아니오", style: UIAlertAction.Style.default, handler: nil)
                
                me.addAction(ac)
                me.addAction(ac2)
                
                self.present(me, animated: true, completion: nil)
                
            }
            
        } )
        btn.addAction(btnAction1)
        btn.addAction(btnAction2)
        present(btn, animated: true, completion: nil)
        
        
    }
    
    
    @IBAction func btnRemove(_ sender: Any) {
        
        let btn = UIAlertController(title: "램프제거", message: "램프를 제거하시겠습니까?", preferredStyle: UIAlertController.Style.alert)
        
        let m1 = UIAlertAction(title: "아니요 켤게요", style: UIAlertAction.Style.default, handler: {(_) in
            let btnChoice = UIAlertController(title: "버튼선택", message:"버튼을 선택하세요" , preferredStyle: UIAlertController.Style.alert)
            
            let btnAction1 = UIAlertAction(title: "전구1", style: UIAlertAction.Style.default, handler:{(action) in
                if(self.lamp1 == true){
                    let me = UIAlertController(title: "경고", message: "이미 전구가 켜져있습니다.", preferredStyle: UIAlertController.Style.alert)
                    let ac = UIAlertAction(title: "확인", style: UIAlertAction.Style.default, handler: nil)
                    
                    me.addAction(ac)
                    
                    self.present(me, animated: true, completion: nil)
                }
                else{
                    self.imgView1.image = self.img1
                    self.lamp1 = true
                }
            } )
            
            let btnAction2 = UIAlertAction(title: "전구2", style:UIAlertAction.Style.default, handler:{(action) in
                if(self.lamp2==true){
                    let me = UIAlertController(title: "경고", message: "이미 전구가 켜져있습니다.", preferredStyle: UIAlertController.Style.alert)
                    
                    let ac = UIAlertAction(title: "확인", style: UIAlertAction.Style.default, handler: nil)
                    me.addAction(ac)
                    
                    self.present(me, animated: true, completion: nil)
                }
                else{
                    self.imgView2.image = self.img1
                    self.lamp2 = true
                }
                
            }
            )
            btnChoice.addAction(btnAction1)
            btnChoice.addAction(btnAction2)
            self.present(btnChoice, animated: true, completion: nil)
            
        })
        
        let m2 = UIAlertAction(title: "아니요 끌게요", style: UIAlertAction.Style.default, handler: {(_) in
            let btn1 = UIAlertController(title: "선택", message: "버튼을 선택하세요.", preferredStyle: UIAlertController.Style.alert)
            
            let btnAction1 = UIAlertAction(title: "전구1", style: UIAlertAction.Style.default,
                                           handler: {(_) in
                if(self.lamp1 == true){
                    let me1 = UIAlertController(title: "경고", message: "전구를 끌 것입니까?", preferredStyle: UIAlertController.Style.alert)
                    let ac1 = UIAlertAction(title: "네", style: UIAlertAction.Style.default, handler: {(_) in
                        self.imgView1.image = self.img2
                        self.lamp1 = false
                        
                    })
                    
                    let ac2 = UIAlertAction(title: "아니오", style: UIAlertAction.Style.default, handler: nil)
                    
                    me1.addAction(ac1)
                    me1.addAction(ac2)
                    
                    self.present(me1, animated: true, completion: nil)
                }
                
            })
            
            let btnAction2 = UIAlertAction(title: "전구2", style:UIAlertAction.Style.default, handler: {(_) in
                if(self.lamp2 == true){
                    let me = UIAlertController(title: "경고", message: "전구를 끌 것입니까?", preferredStyle: UIAlertController.Style.alert)
                    
                    let ac = UIAlertAction(title: "네", style: UIAlertAction.Style.default, handler: {(_) in
                        self.imgView2.image = self.img2
                        self.lamp2 = false
                        
                    })
                    let ac2 = UIAlertAction(title: "아니오", style: UIAlertAction.Style.default, handler: nil)
                    
                    me.addAction(ac)
                    me.addAction(ac2)
                    
                    self.present(me, animated: true, completion: nil)
                    
                }
                
            } )
            btn1.addAction(btnAction1)
            btn1.addAction(btnAction2)
            self.present(btn1, animated: true, completion: nil)
            
        })
        
        let m3 = UIAlertAction(title: "제거하겠습니다.", style: UIAlertAction.Style.default, handler: {(_) in
            let me = UIAlertController(title: "선택", message: "버튼을 선택하세요.", preferredStyle: UIAlertController.Style.alert)
            
            let ac = UIAlertAction(title: "전구1", style: UIAlertAction.Style.default, handler: {(_) in
                self.imgView1.image = self.img3
                self.lamp1 = false
            })
            
            let ac1 = UIAlertAction(title: "전구2", style: UIAlertAction.Style.default, handler: {(_) in
                self.imgView2.image = self.img3
                self.lamp2 = false
                
            })
            me.addAction(ac)
            me.addAction(ac1)
            self.present(me, animated: true,completion: nil)
        })
        btn.addAction(m1)
        btn.addAction(m2)
        btn.addAction(m3)
        present(btn, animated: true, completion: nil)
    }
}
