//
//  ViewController.swift
//  Web
//
//  Created by CYS on 2022/12/01.
//

import UIKit
import WebKit

class ViewController: UIViewController, WKNavigationDelegate {

    @IBOutlet var myWebView: WKWebView!
    @IBOutlet var txtUrl: UITextField!
    @IBOutlet var myActivityIndicator: UIActivityIndicatorView!
    
    func loadWebPage(_ url:String){
        let myUrl = URL(string: url)
        let myRequest = URLRequest(url: myUrl!)
        
        myWebView.load(myRequest)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        myWebView.navigationDelegate = self
        self.loadWebPage("http://www.google.com")
    }
    
    func webView(_ webView: WKWebView, didCommit navigation: WKNavigation!) {
        myActivityIndicator.startAnimating()
        myActivityIndicator.isHidden = false
    }
    
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        myActivityIndicator.startAnimating()
        myActivityIndicator.isHidden = true
    }
    
    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        myActivityIndicator.startAnimating()
        myActivityIndicator.isHidden = true
    }

    func checkUrl(_ url: String) -> String{
        var strUrl = url
        let flag = strUrl.hasPrefix("http://") // 변수 strUrl가 "http://" 문자열로 시작하는지 확인
        
        if !flag{
            strUrl = "http://" + strUrl
        }
        
        return strUrl
    }

    @IBAction func btnGotoUrl(_ sender: UIButton) {
        let myUrl = self.checkUrl(txtUrl.text!)
        
        txtUrl.text = ""
        loadWebPage(myUrl)
    }
    
    @IBAction func btnGoSite1(_ sender: UIButton) {
        loadWebPage("http://www.smu.ac.kr")
    }
    
    @IBAction func btnGoSite2(_ sender: UIButton) {
        loadWebPage("http://software.smu.ac.kr")
    }
    
    @IBAction func btnLoadHtmlString(_ sender: UIButton) {
        let htmlString = """
                        <h1> HTML FILE </h1>
                        <p> HTML file을 이용한 웹 페이지 </p>
                        <p><a href="http://www.smu.ac.kr">상명대학교</a>로 이동</p>
                        <p><a href="http://software.smu.ac.kr">상명대학교 소프트웨어학과</a>로 이동</p>
                        """
        
        myWebView.loadHTMLString(htmlString, baseURL: nil)
    }
    
    @IBAction func btnLoadHtmlFile(_ sender: UIButton) {
        // 프로젝트 내의 htmlView.html 파일 경로 생성
        let filePath = Bundle.main.path(forResource: "htmlView", ofType: "html")
        // 프로젝트 내의 htmlView.html 파일 경로에 대한 URL 생성
        let myUrl = URL(fileURLWithPath: filePath!)
        let myRequest = URLRequest(url: myUrl)
        
        myWebView.load(myRequest) // HTML 파일을 WebKit View에 로딩
    }
    
    
    @IBAction func btnStop(_ sender: UIBarButtonItem) {
        myWebView.stopLoading()
    }
    
    
    @IBAction func btnReload(_ sender: UIBarButtonItem) {
        myWebView.reload()
    }
    
    @IBAction func btnGoBack(_ sender: UIBarButtonItem) {
        myWebView.goBack()
    }
    
    
    @IBAction func btnGoForward(_ sender: UIBarButtonItem) {
        myWebView.goForward()
    }
}

