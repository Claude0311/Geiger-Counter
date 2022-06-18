#include <stdio.h>
#include <TCanvas.h>
#include <TH2F.h>
#include <TGraphErrors.h>
#include <TF1.h>
#include <TLegend.h>

// using namespace std;

int main() {
    draw_tunnel();
    return 0;
}

void draw_tunnel() {
    set_style();

    TCanvas *c1 = new TCanvas("c1", "Muon Rate vs. Rock Depth", 200, 10, 600, 500);
    c1 -> SetGrid();

    const Int_t n = 7;
    Float_t x[n];

    Float_t count_raw[n]  = {124, 23,  8,  8,  9,  8, 12};
    Float_t t_duration[n] = { 20, 10, 10, 10, 15, 15, 10};
    Float_t distance[n]   = {  0,  5, 15, 25, 35, 40, 45};
    Float_t altitude[n]   = { 23, 26, 30, 31, 33, 37, 41};

    Float_t y[n];
    Float_t ex[n];
    Float_t ey[n];
    Float_t rho_standard = 2.67;
    Float_t base_altitude = 23.;
    for(int i = 0; i < n; ++i) {
        y[i] = count_raw[i] / t_duration[i];
        ey[i] = sqrt(count_raw[i]) / t_duration[i];

        if(i == 0) x[i] = 0;
        else x[i] = (altitude[i] - base_altitude) * rho_standard * 100.;
        printf("%g %g \n", x[i], y[i]);
    }

    TH2F *bk = new TH2F("bk", "bk", 2, -500, 22000, 2, 0.01, 6);
    bk -> Draw();
    bk -> SetXTitle("Rock Depth (g/cm^2)");
    bk -> SetYTitle("Muon Rate (counts/min)");
    bk -> GetXaxis() -> CenterTitle();
    bk -> GetYaxis() -> CenterTitle();

    TGraphErrors *gr = new TGraphErrors(n, x, y, ex, ey);
    gr -> SetTitle("TGraphError Example");
    gr -> SetMarkerColor(4);
    gr -> SetMarkerStyle(21);
    gr -> Draw("P");

    TF1 *p_surv = new TF1("p_surv", muon_surv_prob, 30, 25000, 1);
    p_surv -> SetParameter(0, 4.9);
    p_surv -> SetLineColor(2);
    p_surv -> Draw("same");

    aLegend = new TLegend(0.40, 0.67, 0.89, 0.84);
    aLegend -> SetBorderSize(0);
    aLegend -> SetFillColor(0);
    aLegend -> SetTextFont(52);
    aLegend -> AddEntry(gr, "Observed", "pe");
    aLegend -> AddEntry(p_surv, "Muon Survival Prob. in Rock (Scaled)", "1");
    aLegend -> Draw("same");
    c1 -> Update();
}

double muon_surv_prob(double *x, double *par) {
    double slant_depth = x[0];
    double range = 553.4;
    double prob_surv = range / slant_depth;
    double scale = par[0];
    if(prob_surv > 1) prob_surv = 1;
    return prob_surv * scale;
}

void set_style() {
    gStyle -> SetOptFit(0);
    gStyle -> SetOptStat(0);
    gStyle -> SetOptTitle(0);
    gStyle -> SetPadTickX(1);
    gStyle -> SetPadTickY(1);
    gStyle -> SetPadGridX(1);
    gStyle -> SetPadGridY(1);
    gStyle -> SetPadColor(0);

    gStyle -> SetCanvasColor(0);
    gStyle -> SetFrameBorderMode(0);
    gStyle -> SetCanvasBorderMode(0);
    gStyle -> SetPadBorderMode(0);
    gStyle -> SetPadColor(0);
    gStyle -> SetTitleColor(1);
    gStyle -> SetTitleFillColor(0);
    gStyle -> SetStatColor(0);
    gStyle -> SetOptTitle(0);
}
