

void setcolor(TH1F* h, int kcolor);
void setHistInfo(TH1F* h,string title, double mu, double mu_err,double temp, double temp_err, bool flag);
   

void DifferentPDGComparison(){
  //std::cout<< "Hello" <<std::endl;
  //TFile rootFile("test.root","RECREATE");
  //TH2D temperatureVSmuB("TvsMuB","Temperature Vs {#mu_{B}}; #mu_{B} [MeV]; Temperature [MeV]" ,20, 140, 180, 200, -10, 400);
  //TCanvas *c1 = new TCanvas("c1","c1",600,600);
  //TMarker m; 
  //m.SetMarkerSize(3); 
  
  
  TString inputLine; 
  std::ifstream inputFile("/home/idp3/Documents/RHI/STARYields-AllParticles.csv");
  if (!inputFile.is_open()){
	printf("error opening the file \n");
  
  }
  std::string line;

  double mu, temp, volume, energy, mu_err,temp_err,volume_err;
  int xbin, ybin;
  float xmin,ymin,xmax,ymax;
  xbin = 200;
  ybin = 20;
  xmin = 0.;
  xmax = 400.;
  ymin = 140;
  ymax= 180;


   
   TH1F* STAR200;
   TH1F* STAR62;
   TH1F* STAR39;
   TH1F* STAR27;
   TH1F* STAR19;
   TH1F* STAR11;
   bool star200 = false;
   bool star62=false; 
   bool star39 =false; 
   bool star27=false; 
   bool star19 =false; 
   bool star11=false; 
   //STAR39,STAR27,STAR19,STAR11;
 
  while (std::getline(inputFile, line)){
  	inputLine=line;
	if (inputLine.IsWhitespace()) continue;//skip if the line is empty
	if (inputLine.BeginsWith("#")) continue;// skip if the line starts with #
	TObjArray *objArr;
  	objArr = inputLine.Tokenize(",");
  	
  	//I want to plot temperature as a function of Volume and then temperature as a function of MuB. 
  	
  	energy = (((TObjString*)objArr->At(0))->GetString()).Atoi();
      	mu = (((TObjString*)objArr->At(1))->GetString()).Atof();
      	mu_err = (((TObjString*)objArr->At(2))->GetString()).Atof();
    	temp = (((TObjString*)objArr->At(3))->GetString()).Atof();
      	temp_err = (((TObjString*)objArr->At(4))->GetString()).Atof();
      	volume = (((TObjString*)objArr->At(5))->GetString()).Atof();
      	volume_err  = (((TObjString*)objArr->At(6))->GetString()).Atof();
      	
      	
      /*	vector<float> xleft = {10.0, 20.0, 30.0};
      	vector<float> xright = {15.0, 25.0, 35.0};
      	vector<TH1F*> histVec (0); 
      	
      	int numHists = 3;
      	stringstream ss;
      	for (int i = 0; i < numHists; i++)  {
          ss << "histName" << i;
      	  histVec.push_back(new TH1F("ssName.str().c_str()", "ssName.str().c_str()", 1, xleft[i], xright[i])); 
          //reset stringstream here
        }*/
      	
      	
      	//here we want to make a hist for each STAR point!
        if (energy== 200){
        	//setHistInfo(STAR200, "STAR200",mu,mu_err,temp,temp_err,true);
        	STAR200 = new TH1F("STAR200","STAR200",1,mu-mu_err,mu+mu_err);
        	STAR200->SetBinContent(1,temp);
        	STAR200->SetBinError(1,temp_err);
        	setcolor(STAR200, kRed);
        	star200=true;
        	
        
        	//STAR200->Draw("same");
        	//out.push_back(STAR200);
        	//cout<<temp<<endl;
        }
        else if (energy ==62){
        	STAR62 = new TH1F("STAR62","STAR62",1,mu-mu_err,mu+mu_err);
        	STAR62->SetBinContent(1,temp);
        	STAR62->SetBinError(1,temp_err);
        	setcolor(STAR62, kOrange);
        	star62=true;
        }
        else if (energy==39){
        	STAR39 = new TH1F("STAR39","STAR39",1,mu-mu_err,mu+mu_err);
        	STAR39->SetBinContent(1,temp);
        	STAR39->SetBinError(1,temp_err);
        	setcolor(STAR39,kYellow);
        	star39=true;
        
        }
        else if(energy==27){
        	STAR27 = new TH1F("STAR27","STAR27",1,mu-mu_err,mu+mu_err);
        	STAR27->SetBinContent(1,temp);
        	STAR27->SetBinError(1,temp_err);
        	setcolor(STAR27,kGreen);
        	star27=true;
        
        }
	else if(energy==19){
        	STAR19 = new TH1F("STAR19","STAR19",1,mu-mu_err,mu+mu_err);
        	STAR19->SetBinContent(1,temp);
        	STAR19->SetBinError(1,temp_err);
        	setcolor(STAR19,kCyan);
        	star19=true;
        
        }
	else if(energy==11){
        	STAR11 = new TH1F("STAR11","STAR11",1,mu-mu_err,mu+mu_err);
        	STAR11->SetBinContent(1,temp);
        	STAR11->SetBinError(1,temp_err);
        	setcolor(STAR11,kBlue);
        	star11=true;
        
        }

      	
      	//two things i would like to try: doing the plot with histograms th1d and then using tgrapherrors. Ican't tell if it should 
      	//be the same
      	
      	
  	//std::cout <<objArr->GetEntries()<<std::endl;
  	//std::cout <<("%s \n",(((TObjString*)objArr->At(0))->GetString())) <<std::endl;
  	//std::cout <<("%s \n",(((TObjString*)objArr->At(1))->GetString())) <<std::endl;  
  	
  	//for these files if you have 4 entries you didn't use this for the fit
  	//if you have more than 5 entries then it has yield information. 
  		
  } //end of file 
  
   
    TH1F* spacer = new TH1F("spacer","spacer" , 200, 0.0, 400.0);
    TLegend *leg = new TLegend(0.55, 0.6, 0.75, 0.85);
   leg->SetTextSize(0.035);
   leg->SetBorderSize(0);
   if (star200) leg->AddEntry(STAR200, "STAR Au#font[82]{-}Au @ 200 GeV", "pl");
   if (star62) leg->AddEntry(STAR62, "STAR Au#font[82]{-}Au @ 62.4 GeV", "pl");
   if (star39) leg->AddEntry(STAR39, "STAR Au#font[82]{-}Au @ 39.0 GeV", "pl");
   if (star27) leg->AddEntry(STAR27, "STAR Au#font[82]{-}Au @ 27.0 GeV", "pl");
   if (star19) leg->AddEntry(STAR19, "STAR Au#font[82]{-}Au @ 19.6 GeV", "pl");  
   if (star11) leg->AddEntry(STAR11, "STAR Au#font[82]{-}Au @ 11.5 GeV", "pl");  
   leg -> SetTextFont(82);
   //define TCanvas and TPad for plotting
    TCanvas *c1 = new TCanvas("c1", "", 800, 600);
    c1->cd();
       gStyle->SetOptStat(0);
       gStyle->SetPadTickX(1);
       gStyle->SetPadTickY(1);
       TPad *pad1 = new TPad("pad1", "", 0.0, 0.05, 1.0, 1.0);
          pad1->SetBottomMargin(0.15); // Upper and lower plot are joined
          pad1->SetLeftMargin(0.15); // Upper and lower plot are joined
          pad1->SetRightMargin(0.05); // Upper and lower plot are joined
          pad1->SetTopMargin(0.05); // Upper and lower plot are joined
          pad1->Draw();
          pad1->cd(); 
             spacer->SetTitle("");
             spacer->SetMinimum(140.0);
             spacer->SetMaximum(200.0);
             spacer->SetXTitle("#it{#mu}_{B} (MeV)");
             spacer->GetXaxis()->SetTitleSize(0.045);
             spacer->GetXaxis()->SetLabelSize(0.04);
             spacer->GetXaxis()->SetTitleOffset(1.3);
             spacer->GetXaxis()->SetTitleFont(82);
             spacer->GetXaxis()->SetLabelFont(82);
             spacer->SetYTitle("T_{ch} (MeV)");
             spacer->GetYaxis()->SetTitleSize(0.045);
             spacer->GetYaxis()->SetLabelSize(0.04);
             spacer->GetYaxis()->SetTitleOffset(1.2);
             spacer->GetYaxis()->SetTitleFont(82);
             spacer->GetYaxis()->SetLabelFont(82);
             spacer->Draw("same");
   cout<<"Canvas"<<endl;
  STAR200->Draw("same");
  STAR62->Draw("same");
  STAR39->Draw("same");
  STAR27->Draw("same");
  STAR19->Draw("same");
  STAR11->Draw("same");
  //STAR200->Write();
  //STAR62->Write();
  leg->Draw("same");	
  
  //now we want to upload the info from the .txt files. 
  
}

void setcolor(TH1F* h, int kcolor) {
  h->SetLineColor(kcolor);
  h->SetMarkerColor(kcolor);
  h->SetLineWidth(2);
  h->SetMarkerStyle(20);
  h->SetMarkerSize(1.0);
}

void setHistInfo(TH1F* h, string title, double mu, double mu_err,double temp, double temp_err, bool flag){
    h = new TH1F(title.c_str(),title.c_str(),1,mu-mu_err,mu+mu_err);
        	h->SetBinContent(1,temp);
        	h->SetBinError(1,temp_err);
        	//setcolor(h, kRed);
        	flag=true;

}

