//
//  ViewController.swift
//  project
//
//  Created by CYS on 2022/12/15.
//

import UIKit
import WebKit

class ViewController: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource, WKNavigationDelegate {
    
    var component1 = ["Google","Naver","Daum","YouTube"]
    var c1Url = ["https://www.google.com","https://www.naver.com","https://www.daum.net","https://www.youtube.com"]
    var component2 = ["소프트웨어학과","e-campus","상명대"]
    var c2Url = ["https://software.smu.ac.kr","https://ecampus.smu.ac.kr","https://www.smu.ac.kr"]
    var check = false

    @IBOutlet var webView1: WKWebView!
    @IBOutlet var webView2: WKWebView!
    
    @IBOutlet var indi2: UIActivityIndicatorView!
    @IBOutlet var indi1: UIActivityIndicatorView!
    @IBOutlet var pickerView: UIPickerView!
    func loadWebpage1(_ url:String){
        var myurl = URL(string: url)
        var checkurl = URLRequest(url: myurl!)
        
        webView1.load(checkurl)
        
    }
    
    func loadWebpage2(_ url: String){
        var myurl = URL(string: url)
        var checkurl = URLRequest(url: myurl!)
        
        webView2.load(checkurl)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        webView1.navigationDelegate = self
        webView2.navigationDelegate = self
        
        loadWebpage1("https://www.google.com")
        loadWebpage2("https://software.smu.ac.kr")
    }
    
    func webView(_ webView: WKWebView, didCommit navigation: WKNavigation!) {
        if(webView == webView1){
            indi1.startAnimating()
            indi1.isHidden = false
        }
        else{
            indi2.startAnimating()
            indi2.isHidden = false
            check = false
        }
    }
    
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        if(webView == webView1){
            indi1.stopAnimating()
            indi1.isHidden = true
        }
        else{
            indi2.stopAnimating()
            indi2.isHidden = true
            check = true
        }
    }
    
    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        if(webView == webView1){
            indi1.stopAnimating()
            indi1.isHidden = true
        }
        else{
            indi2.stopAnimating()
            indi2.isHidden = true
        }
    }
    
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 2
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        if(component == 0){
            return 4
        }
        else{
            return 3
        }
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        if(component == 0){
            return component1[row]
        }
        else{
            return component2[row]
        }
    }
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        if(component == 0){
            loadWebpage1(c1Url[row])
        }
        else{
            if(c2Url[row] == "https://www.smu.ac.kr"){
                self.loadWebpage2("https://www.smu.ac.kr")
                if(check == true){
                    let btn = UIAlertController(title: "상명대 사이트 이동", message: "이동하시겠습니까?", preferredStyle: UIAlertController.Style.alert)
                    let ac1 = UIAlertAction(title: "아니오", style: UIAlertAction.Style.default, handler: {(_) in
                        self.loadWebpage2("https://www.smu.ac.kr")
                    })
                    let ac2 = UIAlertAction(title: "소프트웨어학과", style:UIAlertAction.Style.default, handler: {(_) in
                        self.loadWebpage2("https://software.smu.ac.kr")
                    } )
                    let ac3 = UIAlertAction(title: "e-campus", style: UIAlertAction.Style.default, handler: {(_) in
                        self.loadWebpage2("https://ecampus.smu.ac.kr")
                    })
                    
                    btn.addAction(ac1)
                    btn.addAction(ac2)
                    btn.addAction(ac3)
                    
                    present(btn, animated: true, completion: nil)
                    check = false
                }
                
            }
            else{
                loadWebpage2(c2Url[row])
            }
        }
    }
    
    
    
}

